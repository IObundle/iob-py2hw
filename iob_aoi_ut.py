from iob_aoi import iob_aoi
from iob_wire import iob_wire
import copy

def create_subclass(cls,param_dict):
    """Create subclass of the AOI module"""
    new_instances = copy.deepcopy(cls.instances)
    for instance in new_instances:
        new_instances[instance]['module'] = create_subclass(new_instances[instance]['module'],param_dict)
    new_class = type(f"{cls.__name__}_{param_dict['W']}", (cls,), 
                     {'param_dict': param_dict,
                      'instances': new_instances,
                      'description': f"AOI module with {param_dict['W']}-bit operands and result"})
    # Change the name of the class in globals
    globals()[f"{cls.__name__}_{param_dict['W']}"] = new_class
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
