from iob_module import iob_module
from iob_port import iob_port
from iob_wire import iob_wire
from iob_and import iob_and
from iob_or import iob_or
from iob_inv import iob_inv

class iob_aoi(iob_module):
    """AOI module class"""
    # Default ports and parameters
    ports = {'i': 'input',
            'o0': 'output'}
    params = [{'name': 'W', 'min_value': 1, 'max_value': 32},
            {'name': 'N', 'min_value': 4, 'max_value': 4}]

    def __init__(self, name, ports, params, suffix):
        """Constructor for AOI module"""
        # Call iob_module constructor
        super().__init__(name, ports, params, suffix)
        # Create wires
        and0_out = self.create_wire('and0_out', params['W'], 0)
        and1_out = self.create_wire('and1_out', params['W'], 0)
        or0_out = self.create_wire('or0_out', params['W'], 0)
        
        # Create param_dict for AND0
        and0_param_dict = {'W': params['W'], 'N': 2}
        # Create param_dict for AND1
        and1_param_dict = {'W': params['W'], 'N': 2}
        # Create param_dict for OR0
        or0_param_dict = {'W': params['W'], 'N': 2}
        # Create param_dict for INV0
        inv0_param_dict = {'W': params['W'], 'N': 1}

        # Create AND0 port_list
        and0_port_list = [{'name': 'i0', 'wire': self.i0.wire(), 'direction': 'input'},
                            {'name': 'i1', 'wire': self.i1.wire(), 'direction': 'input'},
                            {'name': 'o0', 'wire': and0_out, 'direction': 'output'}]
        # Create AND1 port_list
        and1_port_list = [{'name': 'i0', 'wire': self.i2.wire(), 'direction': 'input'},
                            {'name': 'i1', 'wire': self.i3.wire(), 'direction': 'input'},
                            {'name': 'o0', 'wire': and1_out, 'direction': 'output'}]
        # Create OR0 port_list
        or0_port_list = [{'name': 'i0', 'wire': and0_out, 'direction': 'input'},
                            {'name': 'i1', 'wire': and1_out, 'direction': 'input'},
                            {'name': 'o0', 'wire': or0_out, 'direction': 'output'}]
        # Create INV0 port_list
        inv0_port_list = [{'name': 'i0', 'wire': or0_out, 'direction': 'input'},
                            {'name': 'o0', 'wire': self.o0.wire(), 'direction': 'output'}]

        # Create AND0 module
        and0 = self.create_instance(iob_and, 'and0', and0_port_list, and0_param_dict, '_aoi_in')
        # Create AND1 module
        and1 = self.create_instance(iob_and, 'and1', and1_port_list, and1_param_dict, '_aoi_in')
        # Create OR0 module
        or0 = self.create_instance(iob_or, 'or0', or0_port_list, or0_param_dict, '_aoi_mid')
        # Create INV0 module
        inv0 = self.create_instance(iob_inv, 'inv0', inv0_port_list, inv0_param_dict, '_aoi_out')

        
         

def unit_test():
    '''Unit test for AOI module'''
    # Create 5 wires
    w0 = iob_wire('w0', 2, 0)
    w1 = iob_wire('w1', 2, 0)
    w2 = iob_wire('w2', 2, 0)
    w3 = iob_wire('w3', 2, 0)
    w4 = iob_wire('w4', 2, 0)

    # Create module
    aoi0 = iob_aoi('aoi0', [{'name': 'i0', 'wire': w0, 'direction': 'input'},
                            {'name': 'i1', 'wire': w1, 'direction': 'input'},
                            {'name': 'i2', 'wire': w2, 'direction': 'input'},
                            {'name': 'i3', 'wire': w3, 'direction': 'input'},
                            {'name': 'o0', 'wire': w4, 'direction': 'output'}],
                            {'W': 2, 'N': 4}, '_aoi')
    
    # Print module
    aoi0.print_verilog_module()
    # Print module instance
    aoi0.print_verilog_module_inst()
    
if __name__ == "__main__":
    unit_test()
