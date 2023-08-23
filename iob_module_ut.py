from iob_module import iob_module
from iob_wire import iob_wire
import copy
    
def unit_test():
    width = 7
    
    w0 = iob_wire(name='w0', width=width)
    w1 = iob_wire(name='w1', width=width)
    
    m0 = iob_module.new_instance(
        description = "This is a test module",
        param_dict = {'W': width},
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
