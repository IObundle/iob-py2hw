from iob_param import iob_param
from iob_port import iob_port
from iob_wire import iob_wire

class iob_module:
    """Class to represent a Verilog module"""
    def __init__(self, name, port_list, param_list=[], wire_list=[], inst_list=[]):
        self.name = name
        self.port_list = port_list
        self.param_list = param_list
        self.wire_list = wire_list
        self.inst_list = inst_list

    @classmethod
    def print_verilog_module(cls, self):
        print(f"module {cls.__name__}(")
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
            i.print_verilog_inst()
            
        print(f"endmodule")

    @classmethod
    def print_verilog_module_inst(cls, self):
        print(f"{cls.__name__} {self.name}")
        print(f"  #(")
        for p in self.param_list:
            #test if the last element
            if p == self.param_list[-1]:
                p.print_param_assign(comma=False)
            else:
                p.print_param(comma=True)
        print(f"  )")
        print(f"{self.name}")
        print(f"  (")
        for p in self.port_list:
            #test if the last element
            if p == self.port_list[-1]:
                p.print_port(comma=False)
            else:
                p.print_port(comma=True)
        print(f"  );")


# test this class
if __name__ == "__main__":

    param_list = [iob_param('W', 32, 1)]

    port_list = [iob_port('clk', 1, '', 'input'), iob_port('rst', 1, '', 'input'), iob_port('in', 32, '', 'input'), iob_port('out', 32, '', 'output')]

    wire_list = [iob_wire('w1', 32), iob_wire('w2', 32)]
    
    iob = iob_module('iob', port_list, param_list, wire_list)
    
    iob.print_verilog_module(iob)

    iob.print_verilog_module_inst(iob)
    
