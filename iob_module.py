from iob_port import iob_port
from iob_wire import iob_wire
import copy

class iob_module:
    """Class to represent a Verilog module"""
    params = [
        {'name': 'W', 'min_value': 1, 'max_value': 32}
    ]
    param_dict = {'W': 1}
    ports = {
        'a0': {'direction':'input', 'width':'W', 'description':'Input port'},
        'o0': {'direction':'output', 'width':'W', 'description':'Output port'}
    }
    wires = {} #{name:widht}
    instances = {} #{name:{'module':module, 'port_map':port_map, 'description':'description'}}
    assigns = {} #{dest: expr}
    description = "Default module description"
    
    def __init__(self, instance_name, port_map, description):
        self.instance_name = instance_name
        self.description = description
        for name, info in self.__class__.ports.items():
            if name not in port_map:
                raise ValueError(f"Port {name} is missing")
            if isinstance(info['width'],str):
                width = self.__class__.param_dict[info['width']]
            elif not isinstance(info['width'],int):
                raise ValueError(f"Port {name} width is not valid")
            else:
                width = info['width']
            port = self.create_port(name, width, info['direction'])
            port.connect(port_map[name])
        for name, w in self.__class__.wires.items():
            if isinstance(w,str):
                width = self.__class__.param_dict[w]
            elif not isinstance(w,int):
                raise ValueError(f"Wire {name} width is not valid")
            else:
                width = w
            wire = self.create_wire(name, width)
        self.assign_list = []
        for name, expr in self.__class__.assigns.items():
            self.create_assign(name, expr)
        self.inst_list = []
        for name, info in self.__class__.instances.items():
            port_map = copy.deepcopy(info['port_map'])
            for p in port_map:
                if isinstance(port_map[p],str):
                    port_map[p] = getattr(self, port_map[p])
            inst = self.create_instance(info['module'], name, port_map, info['description'])

    def create_wire(self, name, width):
        """Create a wire"""
        wire = iob_wire(name=name, width=width)
        setattr(self, name, wire)
        return wire

    def create_port(self, name, width, direction):
        """Create a port"""
        port = iob_port(name, width, direction)
        setattr(self, name, port)
        return port

    def create_instance(self, module, instance_name, port_map, description):
        """Create an instance of a module"""
        inst = module(instance_name, port_map, description)
        self.inst_list.append(inst)
        return inst

    def create_assign(self, dest, expr):
        """Create an assignment statement"""
        assign = f'  assign {dest} = {expr};'
        value_list = [attr for attr in vars(self).values() if isinstance(attr, iob_wire)]
        for v in value_list: 
            expr = expr.replace(v.name, f'self.{v.name}')
        getattr(self, dest).set_value(eval(expr))
        self.assign_list.append(assign)
        return assign

    @classmethod
    def create(cls, param_dict, instance_name, port_map, description):
        """Create a new instance of the module and the necessary subclasses"""
        new_class = cls.create_subclass(param_dict)
        inst = new_class(instance_name=instance_name, port_map=port_map, description=description)
        return inst

    @classmethod
    def create_subclass(cls, param_dict):
        new_instances = copy.deepcopy(cls.instances)
        for instance in new_instances:
            new_instances[instance]['module'] = cls.instances[instance]['module'].create_subclass(param_dict)
        new_class = type(f"{cls.__name__}_{param_dict['W']}", (cls,), 
                         {'param_dict': param_dict,
                          'instances': new_instances,
                          'description': f"{cls.__name__} module with {param_dict['W']}-bit operands and result"})
        # Change the name of the class in globals
        globals()[f"{cls.__name__}_{param_dict['W']}"] = new_class
        return new_class
        
    
            
    @classmethod
    def check_params(cls, params):
        """Check if the params are valid for the module"""
        # Check number of params
        if len(params) != len(cls.params):
            raise ValueError(f"Wrong number of params")
        for p in params:
            for i in cls.params:
                if p == i['name']:
                    if params[p] < i['min_value'] or params[p] > i['max_value']:
                        raise ValueError(f"Param {p} has wrong value")
                    break
            else:
                raise ValueError(f"Param {p} is not valid for {cls.__name__}")
            
    def print_verilog_module(self):
        print(f"module {self.__class__.__name__}")
        print(f"  (")
        # Filter attributes of type iob_port using vars() using list comprehention
        port_list = [attr for attr in vars(self).values() if isinstance(attr, iob_port)]
        for p in port_list:
            #test if the last element
            if p is port_list[-1]:
                p.print_port(comma=False)
            else:
                p.print_port(comma=True)
        print(f"  );")
        wire_list = [attr for attr in vars(self).values() if (isinstance(attr, iob_wire) and not isinstance(attr, iob_port))]
        for w in wire_list:
            w.print_wire()

        for a in self.assign_list:
            print(a)

        for i in self.inst_list:
            i.print_verilog_module_inst()
            
        print(f"endmodule")

    def print_verilog_module_inst(self):
        print(f"{self.__class__.__name__} {self.instance_name}")
        print(f"  (")
        # Filter attributes of type iob_port using vars() using list comprehention
        port_list = [attr for attr in vars(self).values() if isinstance(attr, iob_port)]
        for p in port_list:
            #test if the last element
            if p is port_list[-1]:
                p.print_port_assign(comma=False)
            else:
                p.print_port_assign(comma=True)
        print(f"  );")
