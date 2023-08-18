from iob_module import iob_module
from iob_port import iob_port
from iob_wire import iob_wire


class iob_and(iob_module):
    '''Class for the AND gate module'''
    params = [
        {'name': 'W', 'min_value': 1, 'max_value': 32, 'description': 'Bit width of signals'}
    ]
    param_dict = {'W': 1}
    ports = {
        'i0': {'direction':'input', 'width': 'W', 'description':'Operand 0'},
        'i1': {'direction':'input', 'width': 'W', 'description':'Operand 1'},
        'o0': {'direction':'output', 'width': 'W', 'description':'Result'}
    }
    assigns = {'o0':'i0 & i1'} #{dest: expr}
    descriprion = "General bit-wise AND gate with default 1-bit operands and result"
    
def unit_test():
    """Unit test for iob_and"""

    width = 6
    
    # Create 3 wires
    w0 = iob_wire(name='w0', width=width)
    w0.set_value(0)
    w1 = iob_wire(name='w1', width=width)
    w1.set_value(0)
    w2 = iob_wire(name='w2', width=width)

    iob_and_6 = type(f'iob_and_{width}', (iob_and,), 
                     {'param_dict':{'W':width},
                      'descriprion':f'2-input bit-wise AND gate with {width} bit operands and result'})
    
    # Create an instance
    and0 = iob_and_6(
        description=f'2-input bit-wise AND gate with {width} bit operands and result',
        instance_name = 'and0',
        port_map = {
            'i0': w0, 
            'i1': w1,
            'o0': w2
        }
    )
                            
    and0.print_verilog_module()
    and0.print_verilog_module_inst()

#Test
if __name__ == '__main__':
    unit_test()
