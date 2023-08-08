from iob_module import iob_module
from iob_port import iob_port
from iob_wire import iob_wire


class iob_inv(iob_module):
    '''Class for the INV gate module'''
    params = [
        {'name': 'W', 'min_value': 1, 'max_value': 32, 'description': 'Bit width of inputs'}
    ]
    ports = {
        'i0': {'direction':'input', 'description':'Input port'},
        'o0': {'direction':'output', 'description':'Output port'}
    }
def unit_test():
    """Unit test for iob_inv"""

    # Create 2 wires
    w0 = iob_wire(name='w0', width=1, value=0)
    w1 = iob_wire(name='w1', width=1, value=0)
    
    # Create module
    inv0 = iob_inv(
        #module
        module_suffix = '_0',
        description = 'INV gate bla bla bla',
        #instance
        instance_name = 'inv0',
        param_dict = {'W': 1},
        port_list = [
            {'name': 'i0', 'direction': 'input', 'connect_to': w0},
            {'name': 'o0', 'direction': 'output', 'connect_to': w1}
        ]
    )

    inv0.print_verilog_module()
    inv0.print_verilog_module_inst()

#Test
if __name__ == '__main__':
    unit_test()
