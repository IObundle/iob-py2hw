from iob_datum import iob_datum

class iob_param(iob_datum):
    '''Class for module parameters'''

    def print_param(self, comma=True):
        """Print the parameter"""
        if comma:
            print(f"      parameter [{self.width}-1:0] {self.name} = {self.value},")
        else:
            print(f"      parameter [{self.width}-1:0] {self.name} = {self.value}")

    def print_param_assign(self, comma=True):
        """Print the parameter assignment"""
        if comma:
            print(f"      .{self.name}({self.value}),")
        else:
            print(f"      .{self.name}({self.value})")


def unit_test():
    """Unit test for iob_param"""
    
    # Print title
    print("Unit test for iob_param:")

    # Create a parameter
    param0 = iob_param("WIDTH", 32, 6)
    # Check if the parameter is correct
    assert param0.name == "WIDTH"
    assert param0.width == 32
    assert param0.value == 6

    # Print the parameter
    param0.print_param()

    # Print the parameter instantiation
    param0.print_param_assign()

    # Print end of unit test
    print("End of unit test for iob_param.\n")
    
# Test the class
if __name__ == "__main__":
    unit_test()
