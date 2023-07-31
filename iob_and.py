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

        # Check if the port matrix has the expected number of inputs, outputs, and inouts
        self.check_ports(port_matrix, 1, 1, 0)

        self.param_list = []
        for i in range(len(param_matrix)):
            self.param_list.append(
                iob_param(
                    param_matrix[i][0],
                    param_matrix[i][1],
                    param_matrix[i][2])
            )
            if param_matrix[i][0] == 'W':
                W = param_matrix[i][2]
            elif param_matrix[i][0] == 'N':
                N = param_matrix[i][2]
        
        for i in range(len(port_matrix)):
            # If port is input, check if is called "i0", if not, raise error
            if port_matrix[i][0] == 'input':
                if port_matrix[i][1] != 'i0':
                    raise ValueError('Input port must be called "i0"')
                if port_matrix[i][2] != N*W:
                    raise ValueError('Input port width must be equal to N*W')
            # If port is output, check if is called "o0", if not, raise error
            elif port_matrix[i][0] == 'output':
                if port_matrix[i][1] != 'o0':
                    raise ValueError('Output port must be called "o0"')
                if port_matrix[i][2] != W:
                    raise ValueError('Output port width must be equal to W')

            self.port_list.append(
                iob_port(
                    port_matrix[i][1],
                    port_matrix[i][2],
                    port_matrix[i][0])
            )
            self.port_list[i].connect(port_matrix[i][3])
            
        super().__init__(name, self.port_list, self.param_list)
            

def unit_test():
    """Unit test for iob_and"""
    
    # Create 3 wires
    wire0 = iob_wire("wire0", 2, 1)
    wire1 = iob_wire("wire1", 'W', 2)
    wire2 = iob_wire("wire2", 1, 3)

    # Create iob_and instance
    and0 = iob_and(
        name = 'and0',
        port_matrix = [
            ['input', 'i0', 2, wire0],
            ['output', 'o0', 1, wire2]
        ],
        param_matrix = [
            ['W', 32, 1],
            ['N', 32, 2]
        ]
    )

    # Check if iob_and instance is correct
    assert and0.name == 'and0'
    assert and0.port_list[0].name == 'i0'
    assert and0.port_list[0].width == 2
    assert and0.port_list[0].value == wire0
    assert and0.port_list[0].direction == 'input'

    assert and0.port_list[1].name == 'o0'
    assert and0.port_list[1].width == 1
    assert and0.port_list[1].value == wire2
    assert and0.port_list[1].direction == 'output'

    and0.print_verilog_module()
    and0.print_verilog_module_inst()

#Test
if __name__ == '__main__':
    unit_test()
