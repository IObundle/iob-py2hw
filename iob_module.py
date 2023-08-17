from iob_port import iob_port
from iob_wire import iob_wire

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
    
    def __init__(self, instance_name, port_map, description):
        self.instance_name = instance_name
        self.description = description
        for name, info in self.__class__.ports.items():
            if name not in port_map:
                raise ValueError(f"Port {name} is missing")
            if isinstance(info['width'],str):
                info['width'] = self.__class__.param_dict[info['width']]
            elif not isinstance(info['width'],int):
                raise ValueError(f"Port {name} width is not valid")
            port = self.create_port(name, info['width'], info['direction'])
            port.connect(port_map[name])
        for name, width in self.__class__.wires.items():
            value = width * 'x'
            wire = self.create_wire(name, width, value)
        self.assign_list = []
        for name, expr in self.__class__.assigns.items():
            self.create_assign(name, expr)
        self.inst_list = []
        for name, info in self.__class__.instances.items():
            inst = self.create_instance(info['module'], name, info['port_map'], info['description'])

    def create_wire(self, name, width, value):
        """Create a wire"""
        wire = iob_wire(name=name, width=width)
        wire.set_value(value)
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
        assign = f'assign {dest} = {expr};'
        value_list = [attr for attr in vars(self).values() if (isinstance(attr, iob_wire)]
        for v in value_list: 
            expr = expr.replace(v.name, f'self.{v.name}')
        dest.set_value(eval(expr))
        self.assign_list.append(assign)
        return assign
            
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
            if p == port_list[-1]:
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
            if p == port_list[-1]:
                p.print_port_assign(comma=False)
            else:
                p.print_port_assign(comma=True)
        print(f"  );")

def unit_test():
    # Create 2 wires
    w0 = iob_wire(name='w0', width=1)
    w0.set_value('z')
    w1 = iob_wire(name='w1', width=1)
    w1.set_value('x')

    # create module
    m0 = iob_module(
        #module
        description = "This is a test module",
        #instance
        instance_name = 'm0',
        port_map = {
            'a0': w0,
            'o0': w1
        },
    )
                    
    m0.print_verilog_module()
    m0.print_verilog_module_inst()
    
if __name__ == "__main__":
    unit_test()
