from iob_port import iob_port
from iob_wire import iob_wire

class iob_module:
    """Class to represent a Verilog module"""
    # Default ports and parameters
    ports = {'a': 'input',
            'o0': 'output'}
    params = [{'name': 'W', 'min_value': 1, 'max_value': 32},
            {'name': 'N', 'min_value': 2, 'max_value': 32}]
    def __init__(self, name, port_list, param_dict, suffix, wire_list=[], inst_list=[]):
        self.name = name
        self.suffix = suffix
        self.__class__.check_params(param_dict)
        self.param_dict = param_dict
        self.__class__.check_ports(port_list, param_dict)
        self.port_list = []
        for p in port_list:
            if p['direction'] == 'input':
                width = param_dict['W']
            elif p['direction'] == 'output':
                width = param_dict['W']
            port = self.create_port(p['name'], width, p['direction'])
            port.connect(p['wire'])

        self.wire_list = wire_list
        self.inst_list = inst_list

    def creat_wire(self, name, width, value):
        """Create a wire"""
        wire = iob_wire(name, width, value)
        self.wire_list.append(wire)
        return wire

    def create_port(self, name, width, direction):
        """Create a port"""
        port = iob_port(name, width, direction)
        self.port_list.append(port)
        return port

    @classmethod
    def check_ports(cls, ports, params):
        """Check if the ports are valid for the module"""    
        # Check number of ports
        if len(ports) != params['N'] + 1:
            raise ValueError(f"Wrong number of ports")
        # Generate valid port names
        valid_ports = {}
        for v in cls.ports:
            if cls.ports[v] == 'input':
                valid_ports.update({f"{v}{i}": cls.ports[v] for i in range(params['N'])})
            elif cls.ports[v] == 'output':    
                valid_ports.update({f"{v}": cls.ports[v]})
        # Check port names and direction
        for p in ports:
        # Check if port exists
            if p['name'] not in valid_ports:
                raise ValueError(f"Port {p['name']} is not valid for {cls.__name__}")
        # Check port direction
            if valid_ports[p['name']] != p['direction']:
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
        print(f"module {self.__class__.__name__}{self.suffix}")
        print(f"  (")
        for p in self.port_list:
            #test if the last element
            if p == self.port_list[-1]:
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
        print(f"{self.__class__.__name__}{self.suffix} {self.name}")
        print(f"  (")
        for p in self.port_list:
            #test if the last element
            if p == self.port_list[-1]:
                p.print_port_assign(comma=False)
            else:
                p.print_port_assign(comma=True)
        print(f"  );")


# test this class
if __name__ == "__main__":

    # Create 3 wires
    w0 = iob_wire('w0', 1, 0)
    w1 = iob_wire('w1', 1, 0)
    w2 = iob_wire('w2', 1, 0)

    # create module
    m0 = iob_module('m0', [{'name': 'a0', 'direction': 'input', 'wire': w0},
                    {'name': 'a1', 'direction': 'input', 'wire': w1},
                    {'name': 'o0', 'direction': 'output', 'wire': w2}],
                    {'W': 1, 'N': 2}, "_suffix")
                    
    m0.print_verilog_module()
    m0.print_verilog_module_inst()
    
