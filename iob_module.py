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
    def __init__(self, instance_name, port_list, param_dict, module_suffix, description='', wire_list=[], inst_list=[]):
        self.instance_name = instance_name
        self.module_suffix = module_suffix
        self.__class__.check_params(param_dict)
        self.param_dict = param_dict
        self.__class__.check_ports(port_list)
        for p in port_list:
            width = param_dict['W']
            port = self.create_port(p['name'], width, p['direction'])
            port.connect(p['wire'])

        self.wire_list = wire_list
        self.inst_list = inst_list

    def create_wire(self, name, width, value):
        """Create a wire"""
        wire = iob_wire(name, width, value)
        self.wire_list.append(wire)
        return wire

    def create_port(self, name, width, direction):
        """Create a port"""
        port = iob_port(name, width, direction)
        setattr(self, name, port)
        return port

    def create_instance(self, module, name, port_list, param_dict, suffix):
        """Create an instance of a module"""
        inst = module(name, port_list, param_dict, suffix)
        self.inst_list.append(inst)
        return inst

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
        for w in self.wire_list:
            w.print_wire()

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


# test this class
if __name__ == "__main__":

    # Create 2 wires
    w0 = iob_wire(name='w0', width=1, value=0)
    w1 = iob_wire(name='w1', width=1, value=0)

    # create module
    m0 = iob_module(
        #module
        module_suffix = "_suffix",
        description = "This is a test module",
        #instance
        instance_name = 'm0',
        param_dict = {'W': 1},
        port_list = [
            {'name': 'a0', 'direction': 'input', 'wire': w0},
            {'name': 'o0', 'direction': 'output', 'wire': w1}
        ]
    )
                    
    m0.print_verilog_module()
    m0.print_verilog_module_inst()
    
