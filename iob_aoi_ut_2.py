from iob_aoi import iob_aoi
from iob_and import iob_and
from iob_or import iob_or
from iob_inv import iob_inv
from iob_wire import iob_wire
import copy

class iob_and_2(iob_and):
    '''Class for the AND gate module with 2-bit operands and result'''
    param_dict = {'W': 2}
    descriprion = "2-input bit-wise AND gate with 2-bit operands and result"

class iob_or_2(iob_or):
    '''Class for the OR gate module with 2-bit operands and result'''
    param_dict = {'W': 2}
    descriprion = "2-input bit-wise OR gate with 2-bit operands and result"
    
class iob_inv_2(iob_inv):
    '''Class for the INV gate module with 2-bit operands and result'''
    param_dict = {'W': 2}
    descriprion = "2-input bit-wise INV gate with 2-bit operands and result"

class iob_aoi_2(iob_aoi):
    '''Class for the AOI module with 2-bit operands and result'''
    param_dict = {'W': 2}
    descriprion = "2-input bit-wise AOI gate with 2-bit operands and result"
    instances = {
        'and0': {
            'module': iob_and_2,
            'port_map': {
                'i0': 'i0',
                'i1': 'i1',
                'o0': 'and0_o'
            },
            'description': 'AND gate 0'
        },
        'and1': {
            'module': iob_and_2,
            'port_map': {
                'i0': 'i2',
                'i1': 'i3',
                'o0': 'and1_o'
            },
            'description': 'AND gate 1'
        },
        'or0': {
            'module': iob_or_2,
            'port_map': {
                'i0': 'and0_o',
                'i1': 'and1_o',
                'o0': 'or0_o'
            },
            'description': 'OR gate 0'
        },
        'inv0': {
            'module': iob_inv_2,
            'port_map': {
                'i0': 'or0_o',
                'o0': 'o0'
            },
            'description': 'INV gate 0'
        }
    }
        
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
    aoi0 = iob_aoi_2(
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
