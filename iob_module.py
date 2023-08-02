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
        self.port_list = port_list
        self.param_list = param_list
        self.wire_list = wire_list
        self.inst_list = inst_list

    def check_ports(self, ports):
        """Check if the ports are valid for the module"""    
        for p in ports:
        # Check if port exists
            if p not in self.__class__.ports:
                raise ValueError(f"Port {p} is not valid for {self.__class__.__name__}")
        # Check port direction
            if self.__class__.ports[p] != ports[p]:
                raise ValueError(f"Port {p} has wrong direction")

    def check_params(self, params):
        """Check if the params are valid for the module"""
        for p in params:
            for i in self.__class__.params:
                if p == i['name']:
                    if params[p] < i['min_value'] or params[p] > i['max_value']:
                        raise ValueError(f"Param {p} has wrong value")
                    break
            else:
                raise ValueError(f"Param {p['name']} not found in {self.__class__.__name__}")
            
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
    
