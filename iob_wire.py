from iob_datum import iob_datum

class iob_wire(iob_datum):
    """Class to represent a wire in an iob module"""
    def print_wire(self):
        print(f"wire [{self.width}-1:0] {self.name};")

def unit_test():
    """Unit test for iob_wire"""

    # Create a wire
    wire0 = iob_wire("wire0", 8, 1)
    # Check if the wire is correct
    assert wire0.name == "wire0"
    assert wire0.width == 8
    assert wire0.value == 1
    
    # print the wire
    wire0.print_wire()

    # Print end of unit test
    print("End of unit test for iob_wire.")

            
# Test the class
if __name__ == "__main__":
    unit_test()
