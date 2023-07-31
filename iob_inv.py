from iob_module import iob_module
from iob_param import iob_param
from iob_port import iob_port
from iob_wire import iob_wire


class iob_inv(iob_module):
    '''Class for the INV gate module'''
    def __init__(self, name, port_matrix, param_matrix = []):
        '''Constructor for the INV gate module'''
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
        
        for i in range(len(port_matrix)):
            # If port is input, check if is called "i0", if not, raise error
            if port_matrix[i][0] == 'input':
                if port_matrix[i][1] != 'i0':
                    raise ValueError('Input port must be called "i0"')
                if port_matrix[i][2] != W:
                    raise ValueError('Input port width must be equal to W')
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
    """Unit test for iob_inv"""
    
    # Create 2 wires
    wire0 = iob_wire("wire0", 1, 1)
    wire2 = iob_wire("wire2", 1, 3)

    # Create iob_inv instance
    inv0 = iob_inv(
        name = 'inv0',
        port_matrix = [
            ['input', 'i0', 1, wire0],
            ['output', 'o0', 1, wire2]
        ],
        param_matrix = [
            ['W', 32, 1]
        ]
    )

    # Check if iob_inv instance is correct
    assert inv0.name == 'inv0'
    assert inv0.port_list[0].name == 'i0'
    assert inv0.port_list[0].width == 1
    assert inv0.port_list[0].value == wire0
    assert inv0.port_list[0].direction == 'input'

    assert inv0.port_list[1].name == 'o0'
    assert inv0.port_list[1].width == 1
    assert inv0.port_list[1].value == wire2
    assert inv0.port_list[1].direction == 'output'

    inv0.print_verilog_module()
    inv0.print_verilog_module_inst()

#Test
if __name__ == '__main__':
    unit_test()
