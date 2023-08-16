from iob_port import iob_port
from iob_wire import iob_wire

class iob_module:
    """Class to represent a Verilog module"""
    params = [
        {'name': 'W', 'min_value': 1, 'max_value': 32}
    ]
    ports = {
        'a0': {'direction':'input', 'description':'Input port'},
        'o0': {'direction':'output', 'description':'Output port'}
    }
    text_box = ""
    def __init__(self, instance_name, port_list, param_dict, module_suffix, description, inst_list=[], assign_list=[]):
        self.instance_name = instance_name
        self.module_suffix = module_suffix
        self.description = description
        self.__class__.check_params(param_dict)
        self.param_dict = param_dict
        self.__class__.check_ports(port_list)
        for p in port_list:
            width = param_dict['W']
            port = self.create_port(p['name'], width, p['direction'])
            port.connect(p['connect_to'])
        self.inst_list = inst_list
        self.assign_list = assign_list

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

    def create_instance(self, module, instance_name, port_list, param_dict, module_suffix, description):
        """Create an instance of a module"""
        inst = module(instance_name, port_list, param_dict, module_suffix, description)
        self.inst_list.append(inst)
        return inst

    def create_submodule(self, param_dict):
        """Create a subclass representing a module variant"""
        new_class_name = self.__class__.__name__ + '_' + str(param_dict['W'])
        if new_class_name not in globals():
            new_class = type(new_class_name, (self.__class__,), {'params':param_dict})
            globals()[new_class_name] = new_class
            del globals()['new_class']
        else:
            new_class = globals()[new_class_name]
        return new_class

    @classmethod
    def check_ports(cls, ports):
        """Check if the ports are valid for the module"""    
        # Check number of ports
        if len(ports) != len(cls.ports):
            raise ValueError(f"Wrong number of ports")
        # Check port names and direction
        for p in ports:
        # Check if port exists
            if p['name'] not in cls.ports:
                raise ValueError(f"Port {p['name']} is not valid for {cls.__name__}")
        # Check port direction
            if cls.ports[p['name']]['direction'] != p['direction']:
                raise ValueError(f"Port {p['name']} has wrong direction")
            
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
        print(f"module {self.__class__.__name__}{self.module_suffix}")
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

        print(self.__class__.text_box)

        for i in self.inst_list:
            i.print_verilog_module_inst()
            
        print(f"endmodule")

    def print_verilog_module_inst(self):
        print(f"{self.__class__.__name__}{self.module_suffix} {self.instance_name}")
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
    w0 = iob_wire(name='w0', width=3)
    w0.set_value('zzz')
    w1 = iob_wire(name='w1', width=3)
    w1.set_value('xxx')

    # create module
    m0 = iob_module(
        #module
        module_suffix = "_suffix",
        description = "This is a test module",
        #instance
        instance_name = 'm0',
        param_dict = {'W': 3},
        port_list = [
            {'name': 'a0', 'direction': 'input', 'connect_to': w0},
            {'name': 'o0', 'direction': 'output', 'connect_to': w1}
        ]
    )
    
                    
    m0.print_verilog_module()
    m0.print_verilog_module_inst()
    
if __name__ == "__main__":
    unit_test()
