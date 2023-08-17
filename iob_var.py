from iob_wire import iob_wire

class iob_var(iob_wire):
    """Class for a verilog variable"""
    
    def print_verilog(self):
        print(f"  reg [{self.width}-1:0] {self.name};")

def unit_test():
    """Unit test for iob_var"""

    var0 = iob_var(name="var0", width=8)
    var0.set_value(value=17)

    assert var0.name == "var0"
    assert var0.width == 8
    assert var0.value == '00010001'

    var0.print_verilog()

# Test the class
if __name__ == "__main__":
    unit_test()
