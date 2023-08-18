from iob_module import iob_module
from iob_port import iob_port
from iob_wire import iob_wire
from iob_and import iob_and
from iob_or import iob_or
from iob_inv import iob_inv
import copy

class iob_aoi(iob_module):
    """AOI module class. Contains 2 AND gates (AND0 and AND1), 1 OR gate (OR0), and 1 INVERTER gate (INV0). 
    Performs the following operation: o0 = ~((i0 & i1) | (i2 & i3))."""
    params = [
        {'name': 'W', 'min_value': 1, 'max_value': 32, 'description': 'Bit width of input and output ports'}
    ]
    param_dict = {'W': 1}
    ports = {
        'i0': {'direction':'input', 'width': 'W', 'description':'Operand 0 for or AND0'},
        'i1': {'direction':'input', 'width': 'W', 'description':'Operand 1 for or AND0'},
        'i2': {'direction':'input', 'width': 'W', 'description':'Operand 0 for or AND1'},
        'i3': {'direction':'input', 'width': 'W', 'description':'Operand 1 for or AND1'},
        'o0': {'direction':'output', 'width': 'W', 'description':'Result of the operation'}
    }
    wires = {
        'and0_o':'W',
        'and1_o':'W',
        'or0_o':'W'
    } 
    instances = {
        'and0': {
            'module':iob_and,
            'port_map':{
                'i0':'i0',
                'i1':'i1',
                'o0':'and0_o'
            },
            'description':'AND0 module'
        },
        'and1': {
            'module':iob_and,
            'port_map':{
                'i0':'i2',
                'i1':'i3',
                'o0':'and1_o'
            },
            'description':'AND1 module'
        },
        'or0': {
            'module':iob_or,
            'port_map':{
                'i0':'and0_o',
                'i1':'and1_o',
                'o0':'or0_o'
            },
            'description':'OR0 module'
        },
        'inv0': {
            'module':iob_inv,
            'port_map':{
                'i0':'or0_o',
                'o0':'o0'
            },
            'description':'INV0 module'
        }
    } 
    description = "AOI module with default 1-bit operands and result"

def create_subclass(cls,param_dict):
    """Create subclass of the AOI module"""
    new_instances = copy.deepcopy(cls.instances)
    for instance in new_instances:
        new_instances[instance]['module'] = create_subclass(new_instances[instance]['module'],param_dict)
    new_class = type(f"{cls.__name__}_{param_dict['W']}", (cls,), {'param_dict': param_dict, 'instances': new_instances})
    # Change the name of the class in globals
    globals()["{cls.__name__}_{param_dict['W']"] = new_class
    return new_class
        
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

    module = create_subclass(iob_aoi, {'W': width})

    # Create module
    aoi0 = module(
        description = f'AOI module for {width}-bit operands',
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
