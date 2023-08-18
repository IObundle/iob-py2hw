from iob_or import iob_or
from iob_wire import iob_wire


class iob_or_3(iob_or):
    '''Class for the OR gate module with 3-bit operands and result'''
    param_dict = {'W': 3}
    descriprion = "General bit-wise OR gate with default 1-bit operands and result"

def unit_test():
    """Unit test for iob_or"""

    width = 3
    
    # Create 3 wires
    w0 = iob_wire(name='w0', width=width)
    w0.set_value(0)
    w1 = iob_wire(name='w1', width=width)
    w1.set_value(0)
    w2 = iob_wire(name='w2', width=width)
    w2.set_value(0)
    
    # Create instance
    or0 = iob_or_3(
        #module
        description=f'2-input bit-wise OR gate with {width} bit operands and result',
        #instance
        instance_name = 'or0',
        port_map = {
            'i0': w0,
            'i1': w1,
            'o0': w2
        }
    )                        
    
    or0.print_verilog_module()
    or0.print_verilog_module_inst()

#Test
if __name__ == '__main__':
    unit_test()
