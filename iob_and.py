from iob_module import iob_module
from iob_port import iob_port
from iob_wire import iob_wire


class iob_and(iob_module):
    '''Class for the AND gate module'''
    params = [
        {'name': 'W', 'min_value': 1, 'max_value': 32, 'description': 'Bit width of inputs'}
    ]
    ports = {
        'i0': {'direction':'input', 'description':'Input port'},
        'i1': {'direction':'input', 'description':'Input port'},
        'o0': {'direction':'output', 'description':'Output port'}
    }

def unit_test():
    """Unit test for iob_and"""

    # Create 3 wires
    w0 = iob_wire(name='w0', width=10, value=0)
    w1 = iob_wire(name='w1', width=10, value=0)
    w2 = iob_wire(name='w2', width=10, value=0)
    
    # Create module and instance of the module
    # a variation of class iob_and called iob_and_0
    and0 = iob_and(
        #module
        module_suffix='_0',
        description='AND gate bla bla bla',
        #instance 
        instance_name = 'and0',
        param_dict = {'W': 10},
        port_list = [
            {'name': 'i0', 'direction': 'input', 'connect2wire': w0},
            {'name': 'i1', 'direction': 'input', 'connect2wire': w1},
            {'name': 'o0', 'direction': 'output', 'connect2wire': w2}
        ]
    )
                            
    and0.print_verilog_module()
    and0.print_verilog_module_inst()

#Test
if __name__ == '__main__':
    unit_test()
