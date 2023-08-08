from iob_module import iob_module
from iob_port import iob_port
from iob_wire import iob_wire


class iob_or(iob_module):
    '''Class for the OR gate module'''
    params = [
        {'name': 'W', 'min_value': 1, 'max_value': 32, 'description': 'Bit width of inputs'}
    ]
    ports = {
        'i0': {'direction':'input', 'description':'Input port'},
        'i1': {'direction':'input', 'description':'Input port'},
        'o0': {'direction':'output', 'description':'Output port'}
    }
    
def unit_test():
    """Unit test for iob_or"""

    # Create 3 wires
    w0 = iob_wire(name='w0', width=1, value=0)
    w1 = iob_wire(name='w1', width=1, value=0)
    w2 = iob_wire(name='w2', width=1, value=0)
    
    # Create module
    or0 = iob_or(
        #module
        module_suffix='_0',
        description='OR gate bla bla bla',
        #instance
        instance_name = 'or0',
        param_dict = {'W': 1},
        port_list = [
            {'name': 'i0', 'direction': 'input', 'connect2wire': w0},
            {'name': 'i1', 'direction': 'input', 'connect2wire': w1},
            {'name': 'o0', 'direction': 'output', 'connect2wire': w1}
        ]
    )                        
    
    or0.print_verilog_module()
    or0.print_verilog_module_inst()

#Test
if __name__ == '__main__':
    unit_test()
