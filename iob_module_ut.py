from iob_module import iob_module
from iob_wire import iob_wire
import copy
    
def unit_test():
    # Create 2 wires
    w0 = iob_wire(name='w0', width=1)
    w0.set_value('z')
    w1 = iob_wire(name='w1', width=1)
    w1.set_value('x')

    # create module
    m0 = iob_module(
        #module
        description = "This is a test module",
        #instance
        instance_name = 'm0',
        port_map = {
            'a0': w0,
            'o0': w1
        },
    )
                    
    m0.print_verilog_module()
    m0.print_verilog_module_inst()
    
if __name__ == "__main__":
    unit_test()
