from iob_module import iob_module
from iob_port import iob_port
from iob_wire import iob_wire


class iob_inv(iob_module):
    '''Class for the INV gate module'''
    params = [
        {'name': 'W', 'min_value': 1, 'max_value': 32, 'description': 'Bit width of signals'}
    ]
    param_dict = {'W': 1}
    ports = {
        'i0': {'direction':'input', 'width': 'W', 'description':'Operand 0'},
        'o0': {'direction':'output', 'width': 'W', 'description':'Result'}
    }
    assigns = {'o0':'~i0'} #{dest: expr}
    descriprion = "General bit-wise INV gate with default 1-bit operands and result"

def unit_test():
    """Unit test for iob_inv"""

    # Create 2 wires
    w0 = iob_wire(name='w0', width=1)
    w0.set_value(0)
    w1 = iob_wire(name='w1', width=1)

    width = 1
    
    # Create module variation and an instance
    inv0 = iob_inv(
        #module
        description = f'1-input bit-wise INV gate with {width} bit operand and result',
        #instance
        instance_name = 'inv0',
        port_map = {
            'i0': w0,
            'o0': w1
        }
    )

    inv0.print_verilog_module()
    inv0.print_verilog_module_inst()

#Test
if __name__ == '__main__':
    unit_test()
