from iob_module import iob_module
from iob_port import iob_port
from iob_wire import iob_wire
from iob_and import iob_and
from iob_or import iob_or
from iob_inv import iob_inv

class iob_aoi(iob_module):
    """AOI module class"""
    params = [
        {'name': 'W', 'min_value': 1, 'max_value': 32, 'description': 'Bit width of inputs'}
    ]
    ports = {
        'i0': {'direction':'input', 'description':'Input port for AND0'},
        'i1': {'direction':'input', 'description':'Input port for AND0'},
        'i2': {'direction':'input', 'description':'Input port for AND1'},
        'i3': {'direction':'input', 'description':'Input port for AND1'},
        'o0': {'direction':'output', 'description':'Output port'}
    }

    def __init__(self, instance_name, port_list, param_dict, module_suffix, description):
        """Constructor for AOI module"""
        # Call iob_module constructor
        super().__init__(
            instance_name = instance_name,
            port_list = port_list,
            param_dict = param_dict,
            module_suffix = module_suffix,
            description = description
        )
        # Create wires
        and0_out = self.create_wire(name='and0_out', width=param_dict['W'], value=0)
        and1_out = self.create_wire(name='and1_out', width=param_dict['W'], value=0)
        or0_out = self.create_wire(name='or0_out', width=param_dict['W'], value=0)
        
        # Create param_dict for AND0
        and0_param_dict = {'W': param_dict['W']}
        # Create param_dict for AND1
        and1_param_dict = {'W': param_dict['W']}
        # Create param_dict for OR0
        or0_param_dict = {'W': param_dict['W']}
        # Create param_dict for INV0
        inv0_param_dict = {'W': param_dict['W']}

        # Create AND0 port_list
        and0_port_list = [
            {'name': 'i0', 'wire': self.i0, 'direction': 'input'},
            {'name': 'i1', 'wire': self.i1, 'direction': 'input'},
            {'name': 'o0', 'wire': and0_out, 'direction': 'output'}
        ]
        # Create AND1 port_list
        and1_port_list = [
            {'name': 'i0', 'wire': self.i2, 'direction': 'input'},
            {'name': 'i1', 'wire': self.i3, 'direction': 'input'},
            {'name': 'o0', 'wire': and1_out, 'direction': 'output'}
        ]
        # Create OR0 port_list
        or0_port_list = [
            {'name': 'i0', 'wire': and0_out, 'direction': 'input'},
            {'name': 'i1', 'wire': and1_out, 'direction': 'input'},
            {'name': 'o0', 'wire': or0_out, 'direction': 'output'}
        ]
        # Create INV0 port_list
        inv0_port_list = [
            {'name': 'i0', 'wire': or0_out, 'direction': 'input'},
            {'name': 'o0', 'wire': self.o0, 'direction': 'output'}
        ]

        # Create AND0 module
        and0 = self.create_instance(
            #module
            module = iob_and,
            module_suffix = '_and0',
            description = 'AND0 module',
            #instance
            instance_name = 'and0',
            param_dict = and0_param_dict,
            port_list = and0_port_list
        )
        # Create AND1 module
        and1 = self.create_instance(
            #module
            module = iob_and,
            module_suffix = '_and1',
            description = 'AND1 module',
            #instance
            instance_name = 'and1',
            param_dict = and1_param_dict,
            port_list = and1_port_list
        )
        # Create OR0 module
        or0 = self.create_instance(
            #module
            module = iob_or,
            module_suffix = '_or0',
            description = 'OR0 module',
            #instance
            instance_name = 'or0',
            param_dict = or0_param_dict,
            port_list = or0_port_list
        )
        # Create INV0 module
        inv0 = self.create_instance(
            #module
            module = iob_inv,
            module_suffix = '_inv0',
            description = 'INV0 module',
            #instance
            instance_name = 'inv0',
            param_dict = inv0_param_dict,
            port_list = inv0_port_list
        )
        

def unit_test():
    '''Unit test for AOI module'''
    # Create 5 wires
    w0 = iob_wire(name='w0', width=2, value=0)
    w1 = iob_wire(name='w1', width=2, value=0)
    w2 = iob_wire(name='w2', width=2, value=0)
    w3 = iob_wire(name='w3', width=2, value=0)
    w4 = iob_wire(name='w4', width=2, value=0)

    # Create module
    aoi0 = iob_aoi(
        #module
        module_suffix = '_aoi0',
        description = 'AOI0 module',
        #instance
        instance_name = 'aoi0',
        param_dict = {'W': 2},
        port_list = [
            {'name': 'i0', 'wire': w0, 'direction': 'input'},
            {'name': 'i1', 'wire': w1, 'direction': 'input'},
            {'name': 'i2', 'wire': w2, 'direction': 'input'},
            {'name': 'i3', 'wire': w3, 'direction': 'input'},
            {'name': 'o0', 'wire': w4, 'direction': 'output'}
        ]
    )
    
    aoi0.print_verilog_module()
    aoi0.print_verilog_module_inst()
    
if __name__ == "__main__":
    unit_test()
