from iob_module import iob_module
from iob_param import iob_param
from iob_port import iob_port
from iob_wire import iob_wire


class iob_and(iob_module):
    '''Class for the AND gate module'''
    def __init__(self, name, port_matrix, param_matrix = []):
        '''Constructor for the AND gate module'''
        self.name = name
        self.port_list = []
        for i in range(len(port_matrix)):
            self.port_list.append(
                iob_port(
                    port_matrix[i][1],
                    port_matrix[i][2],
                    port_matrix[i][3],
                    port_matrix[i][0])
            )
        self.param_list = []
        for i in range(len(param_matrix)):
            self.param_list.append(
                iob_param(
                    param_matrix[i][0],
                    param_matrix[i][1],
                    param_matrix[i][2])
            )

        super().__init__(name, self.port_list, self.param_list)
            

def unit_test():
    """Unit test for iob_and"""
    
    # Create 3 wires
    wire0 = iob_wire("wire0", 'W', 1)
    wire1 = iob_wire("wire1", 'W', 2)
    wire2 = iob_wire("wire2", 'W', 3)

    # Create iob_and instance
    and0 = iob_and(
        name = 'and0',
        port_matrix = [
            ['input', 'i0', 'W', wire0],
            ['input', 'i1', 'W', wire1],
            ['output', 'o0', 'W', wire2]
        ],
        param_matrix = [
            ['W', 32, 1],
            ['N', 32, 2]
        ]
    )

    # Check if iob_and instance is correct
    assert and0.name == 'and0'
    assert and0.port_list[0].name == 'i0'
    assert and0.port_list[0].width == 'W'
    assert and0.port_list[0].value == wire0
    assert and0.port_list[0].direction == 'input'

    assert and0.port_list[1].name == 'i1'
    assert and0.port_list[1].width == 'W'
    assert and0.port_list[1].value == wire1
    assert and0.port_list[1].direction == 'input'

    assert and0.port_list[2].name == 'o0'
    assert and0.port_list[2].width == 'W'
    assert and0.port_list[2].value == wire2
    assert and0.port_list[2].direction == 'output'
    
    and0.print_verilog_module(and0)
    and0.print_verilog_module_inst(and0)

#Test
if __name__ == '__main__':
    unit_test()
