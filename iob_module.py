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

    def check_ports(self, port_matrix, expected_inputs, expected_outputs, expected_inouts):
        """Check if the port matrix has the expected number of inputs, outputs, and inouts"""
        # Count the number of inputs, outputs, and inouts
        num_inputs = 0
        num_outputs = 0
        num_inouts = 0
        for i in range(len(port_matrix)):
            if port_matrix[i][0] == "input":
                num_inputs += 1
            elif port_matrix[i][0] == "output":
                num_outputs += 1
            elif port_matrix[i][0] == "inout":
                num_inouts += 1
            else:
                raise Exception(f"Invalid port direction: {port_matrix[i][0]}")

        # Check if the number of inputs, outputs, and inouts are correct
        assert num_inputs == expected_inputs
        assert num_outputs == expected_outputs
        assert num_inouts == expected_inouts

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
                p.print_param(comma=True)
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
    
