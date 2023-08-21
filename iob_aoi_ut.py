from iob_aoi import iob_aoi
from iob_wire import iob_wire
import copy

def unit_test():
    '''Unit test for AOI module'''
    width = 2
    
    # Create 5 wires
    w0 = iob_wire(name='w0', width=width)
    w0.set_value(1)
    w1 = iob_wire(name='w1', width=width)
    w1.set_value(1)
    w2 = iob_wire(name='w2', width=width)
    w2.set_value(1)
    w3 = iob_wire(name='w3', width=width)
    w3.set_value(1)
    w4 = iob_wire(name='w4', width=width)
    w4.set_value(1)

    # Create module
    aoi0 = iob_aoi.new_instance(
        description = f'AOI module for {width}-bit operands',
        param_dict = {'W': width},
        instance_name = 'aoi0',
        port_map = {
            'i0': w0,
            'i1': w1,
            'i2': w2,
            'i3': w3,
            'o0': w4
        }
    )
    
    aoi0.print_verilog_module()
    aoi0.print_verilog_module_inst()
    
if __name__ == "__main__":
    unit_test()
