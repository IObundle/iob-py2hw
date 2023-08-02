from iob_param import iob_param
from iob_port import iob_port
from iob_wire import iob_wire

class iob_module:
    """Class to represent a Verilog module"""
    # Default ports and parameters
    ports = {'i0': 'input',
            'o0': 'output'}
    params = [{'name': 'W', 'min_value': 1, 'max_value': 32},
            {'name': 'N', 'min_value': 2, 'max_value': 32}]
    def __init__(self, name, port_list, param_list=[], wire_list=[], inst_list=[]):
        self.name = name
        self.__class__.check_ports(port_list)
        self.__class__.check_params(param_list)
        self.port_list = []
        for p in port_list:
            if p['direction'] == 'input':
                width = param_list['W'] * param_list['N']
            elif p['direction'] == 'output':
                width = param_list['W']
            port = create_port(p['name'], width, p['direction'])
            port.connect(p['wire'])
            self.port_list.append(port)

        self.param_list = []
        for p in param_list:
            param = create_param(p, param_list[p])
            
        self.wire_list = wire_list
        self.inst_list = inst_list

    def create_port(self, name, width, direction):
        """Create a port"""
        port = iob_port(name, width, direction)
        self.port_list.append(port)
        return port

    def create_param(self, name, value):
        """Create a param"""
        param = iob_param(name, value)
        self.param_list.append(param)
        return param

    @classmethod
    def check_ports(cls, ports):
        """Check if the ports are valid for the module"""    
        # Check number of ports
        if len(ports) != len(cls.ports):
            raise ValueError(f"Wrong number of ports")
        for p in ports:
        # Check if port exists
            if p['name'] not in cls.ports:
                raise ValueError(f"Port {p['name']} is not valid for {cls.__name__}")
        # Check port direction
            if cls.ports[p] != p['direction']:
                raise ValueError(f"Port {p['name']} has wrong direction")

    @classmethod
    def check_params(cls, params):
        """Check if the params are valid for the module"""
        # Check number of params
        if len(params) != len(cls.params):
        for p in params:
            for i in cls.params:
                if p == i['name']:
                    if params[p] < i['min_value'] or params[p] > i['max_value']:
                        raise ValueError(f"Param {p} has wrong value")
                    break
            else:
                raise ValueError(f"Param {p['name']} not found in {cls.__name__}")
            
    def print_verilog_module(self):
        print(f"module {self.__class__.__name__}")
        print(f"  #(")
        for p in self.param_list:
            #test if the last element
            if p == self.param_list[-1]:
                p.print_param(comma=False)
            else:
                p.print_param(comma=True)
        print(f"  )")
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
        print(f"{self.__class__.__name__}")
        print(f"  #(")
        for p in self.param_list:
            #test if the last element
            if p == self.param_list[-1]:
                p.print_param_assign(comma=False)
            else:
                p.print_param_assign(comma=True)
        print(f"  ) {self.name} (")
        for p in self.port_list:
            #test if the last element
            if p == self.port_list[-1]:
                p.print_port_assign(comma=False)
            else:
                p.print_port_assign(comma=True)
        print(f"  );")


# test this class
if __name__ == "__main__":

    param_list = [iob_param('W', 32, 1)]

    port_list = [iob_port('clk', 1, '', 'input'), iob_port('rst', 1, '', 'input'), iob_port('in', 32, '', 'input'), iob_port('out', 32, '', 'output')]

    wire_list = [iob_wire('w1', 32), iob_wire('w2', 32)]
    
    iob = iob_module('iob', port_list, param_list, wire_list)
    
    iob.print_verilog_module()

    iob.print_verilog_module_inst()
    
