from iob_inv import iob_inv
from iob_wire import iob_wire

def unit_test():
    """Unit test for iob_inv"""

    width = 4
    
    # Create 2 wires
    w0 = iob_wire(name='w0', width=width)
    w0.set_value(0)
    w1 = iob_wire(name='w1', width=width)
    
    # Create instance
    inv0 = iob_inv.create(
        description = f'1-input bit-wise INV gate with {width} bit operand and result',
        param_dict={'W': width},
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
