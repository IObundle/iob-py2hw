from iob_module import iob_module
from iob_port import iob_port
from iob_wire import iob_wire


class iob_and(iob_module):
    '''Class for the AND gate module'''
    params = [
        #N cannot easily be handled by iob_module
        #if it is known to iob_module then name should not be passed
        #etc 
        {'name': 'N', 'min_value': 2, 'max_value': 32, 'description': 'Number of inputs'},
        {'name': 'W', 'min_value': 1, 'max_value': 32, 'description': 'Bit width of inputs'},
    ]
    ports = {
        'i': ['input', 'description'],
        'o0': ['output', 'description'],
    }
    #maybe needs a constructor to solve the N problem?


    
def unit_test():
    """Unit test for iob_and"""

    # Create 3 wires
    w0 = iob_wire(name='w0', width=0, value=0)
    w1 = iob_wire('w1', 10, 0)
    w2 = iob_wire('w2', 10, 0)
    
    # Create module and instance of the module
    # a variation of class iob_and called iob_and_0
    and0 = iob_and(
        #module
        module_suffix='_0',
        description='AND gate bla bla bla',
        #instance 
        instance_name = 'and0',
        param_dict {'W': 10, 'N': 2},
        port_list = [{'name': 'i0', 'wire': w0, 'direction': 'input'},
                     {'name': 'i1', 'wire': w1, 'direction': 'input'},
                     {'name': 'o0', 'wire': w2, 'direction': 'output'}],
    )
                            
    and0.print_verilog_module()
    and0.print_verilog_module_inst()

#Test
if __name__ == '__main__':
    unit_test()
