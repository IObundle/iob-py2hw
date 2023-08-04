from iob_module import iob_module
from iob_port import iob_port
from iob_wire import iob_wire


class iob_inv(iob_module):
    '''Class for the INV gate module'''
    # Default ports and parameters
    ports = {'i': 'input',
            'o0': 'output'}
    params = [{'name': 'W', 'min_value': 1, 'max_value': 32},
            {'name': 'N', 'min_value': 1, 'max_value': 1}]

def unit_test():
    """Unit test for iob_inv"""

    # Create 2 wires
    w0 = iob_wire('w0', 1, 0)
    w1 = iob_wire('w1', 1, 0)
    
    # Create module
    inv0 = iob_inv('and0', [{'name': 'i0', 'wire': w0, 'direction': 'input'},
                            {'name': 'o0', 'wire': w1, 'direction': 'output'}],
                            {'W': 1, 'N': 1}, '_0')
                            
    
    inv0.print_verilog_module()
    inv0.print_verilog_module_inst()

#Test
if __name__ == '__main__':
    unit_test()
