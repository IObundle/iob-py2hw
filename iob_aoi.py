from iob_module import iob_module
from iob_port import iob_port
from iob_wire import iob_wire
from iob_and import iob_and
from iob_or import iob_or
from iob_inv import iob_inv

class iob_aoi(iob_module):
    """AOI module class. Contains 2 AND gates (AND0 and AND1), 1 OR gate (OR0), and 1 INVERTER gate (INV0). 
    Performs the following operation: o0 = ~((i0 & i1) | (i2 & i3))."""
    params = [
        {'name': 'W', 'min_value': 1, 'max_value': 32, 'description': 'Bit width of input and output ports'}
    ]
    ports = {
        'i0': {'direction':'input', 'description':'Operand 0 for or AND0'},
        'i1': {'direction':'input', 'description':'Operand 1 for or AND0'},
        'i2': {'direction':'input', 'description':'Operand 0 for or AND1'},
        'i3': {'direction':'input', 'description':'Operand 1 for or AND1'},
        'o0': {'direction':'output', 'description':'Result of the operation'}
    }

    def __init__(self, instance_name, port_list, param_dict, module_suffix, description):
        """Constructor for the AOI module"""
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

        # Create AND0 module
        and0 = self.create_instance(
            #module
            module = iob_and,
            module_suffix = '_and0',
            description = 'AND0 module',
            #instance
            instance_name = 'and0',
            param_dict = {'W': param_dict['W']},
            port_list = [
                {'name': 'i0', 'direction': 'input', 'connect_to': self.i0},
                {'name': 'i1', 'direction': 'input', 'connect_to': self.i1},
                {'name': 'o0', 'direction': 'output', 'connect_to': and0_out}
            ]
        )
        # Create AND1 module
        and1 = self.create_instance(
            #module
            module = iob_and,
            module_suffix = '_and1',
            description = 'AND1 module',
            #instance
            instance_name = 'and1',
            param_dict = {'W': param_dict['W']},
            port_list = [
                {'name': 'i0', 'direction': 'input', 'connect_to': self.i2},
                {'name': 'i1', 'direction': 'input', 'connect_to': self.i3},
                {'name': 'o0', 'direction': 'output', 'connect_to': and1_out}
            ]
        )
        # Create OR0 module
        or0 = self.create_instance(
            #module
            module = iob_or,
            module_suffix = '_or0',
            description = 'OR0 module',
            #instance
            instance_name = 'or0',
            param_dict = {'W': param_dict['W']},
            port_list = [
                {'name': 'i0', 'direction': 'input', 'connect_to': and0_out},
                {'name': 'i1', 'direction': 'input', 'connect_to': and1_out},
                {'name': 'o0', 'direction': 'output', 'connect_to': or0_out}
            ]
        )
        # Create INV0 module
        inv0 = self.create_instance(
            #module
            module = iob_inv,
            module_suffix = '_inv0',
            description = 'INV0 module',
            #instance
            instance_name = 'inv0',
            param_dict = {'W': param_dict['W']},
            port_list = [
                {'name': 'i0', 'direction': 'input', 'connect_to': or0_out},
                {'name': 'o0', 'direction': 'output', 'connect_to': self.o0}
            ]
        )
        

def unit_test():
    '''Unit test for AOI module'''
    # Create 5 wires
    w0 = iob_wire(name='w0', width=2)
    w0.set_value(1)
    w1 = iob_wire(name='w1', width=2)
    w1.set_value(1)
    w2 = iob_wire(name='w2', width=2)
    w2.set_value(1)
    w3 = iob_wire(name='w3', width=2)
    w3.set_value(1)
    w4 = iob_wire(name='w4', width=2)
    w4.set_value(1)

    width = 2

    # Create module
    aoi0 = iob_aoi(
        #module
        module_suffix = '_'+str(width),
        description = f'AOI module for {width}-bit operands',
        #instance
        instance_name = 'aoi0',
        param_dict = {'W': width},
        port_list = [
            {'name': 'i0', 'direction': 'input', 'connect_to': w0},
            {'name': 'i1', 'direction': 'input', 'connect_to': w1},
            {'name': 'i2', 'direction': 'input', 'connect_to': w2},
            {'name': 'i3', 'direction': 'input', 'connect_to': w3},
            {'name': 'o0', 'direction': 'output', 'connect_to': w4}
        ]
    )
    
    aoi0.print_verilog_module()
    aoi0.print_verilog_module_inst()
    
if __name__ == "__main__":
    unit_test()
