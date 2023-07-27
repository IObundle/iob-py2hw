from iob_datum import iob_datum

class iob_param(iob_datum):
    '''Class for module parameters'''

    def print_param(self, comma=True):
        """Print the parameter"""
        if comma:
            print(f"      parameter [{self.width}-1:0] {self.name} = {self.value},")
        else:
            print(f"      parameter [{self.width}-1:0] {self.name} = {self.value}")

    def print_param_assign(self, comma):
        """Print the parameter assignment"""
        if comma:
            print(f"      .{self.name}({self.value}),")
        else:
            print(f"      .{self.name}({self.value})")


# Test the class
if __name__ == "__main__":
    # Create a parameter
    param = iob_param("WIDTH", 32, 6) 
    param.print_param()

