from iob_datum import iob_datum

class iob_wire(iob_datum):
    """Class to represent a wire in an iob module"""
    def print_wire(self):
        print(f"wire [{self.width}-1:0] {self.name};")


            
# Test the class
if __name__ == "__main__":
    # Create a wire
    wire1 = iob_wire("wire1", width=8)
    wire1.print_wire()
    
   

