from iob_module import iob_module
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
