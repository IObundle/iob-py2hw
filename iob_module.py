from iob_param import iob_param
from iob_port import iob_port
from iob_wire import iob_wire

class iob_module:
    """Class to represent a Verilog module"""
    def __init__(self, name, port_list, param_list=[], wire_list=[], inst_list=[]):
        self.name = name
        self.port_list = port_list
        for port in self.port_list:
            if port.width != port.value.width and isinstance(port.width, int):
                raise ValueError(f"Port width {port.width} does not match value width {port.value.width}")
            # if port.width is str, check for parameter with the same name and compare its values
            elif isinstance(port.width, str):
                for param in param_list:
                    if param.name == port.width:
                        if param.value != port.value.width:
                            raise ValueError(f"Parameter value {param.value} does not match port width {port.value.width}")
                        break
                else:
                    param_list.append(iob_param(port.width, 32, port.value.width))
        self.param_list = param_list
        self.wire_list = wire_list
        self.inst_list = inst_list

    @classmethod
    def print_verilog_module(cls, self):
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
            i.print_verilog_inst()
            
        print(f"endmodule")

    @classmethod
    def print_verilog_module_inst(cls, self):
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


def unit_test():
    """Unit test for iob_module"""

    param_list = [iob_param('W', 32, 1)]

    port_list = [iob_port('clk', 1, '', 'input'), iob_port('rst', 1, '', 'input'), iob_port('in', 32, '', 'input'), iob_port('out', 32, '', 'output')]

    wire_list = [iob_wire('w1', 32), iob_wire('w2', 32)]

    iob = iob_module('iob', port_list, param_list, wire_list)

    iob.print_verilog_module(iob)

# test this class
if __name__ == "__main__":
    unit_test()
