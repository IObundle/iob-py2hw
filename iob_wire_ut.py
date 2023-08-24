from iob_wire import iob_wire

def unit_test():
    """Unit test for iob_wire"""

    wire0 = iob_wire(name="wire0", width=8)
    wire0.set_value(value=17)
    
    assert wire0.name == "wire0"
    assert wire0.width == 8
    assert wire0.value == '00010001'
    
    wire0.print_wire()
            
if __name__ == "__main__":
    unit_test()
