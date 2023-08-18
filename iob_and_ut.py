from iob_and import iob_and
from iob_wire import iob_wire

class iob_and_6(iob_and):
    '''Class for the AND gate module with 6-bit operands and result'''
    param_dict = {'W': 6}
    descriprion = "2-input bit-wise AND gate with 6-bit operands and result"
    
def unit_test():
    """Unit test for iob_and"""

    width = 6
    
    # Create 3 wires
    w0 = iob_wire(name='w0', width=width)
    w0.set_value(0)
    w1 = iob_wire(name='w1', width=width)
    w1.set_value(0)
    w2 = iob_wire(name='w2', width=width)

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
