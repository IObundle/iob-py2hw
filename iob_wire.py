class iob_wire:
    """Class to represent a wire in an iob module"""

    def __init__(self, name, width):
        self.name = name
        self.width = width
        self.value = 'x' * width

    def set_value(self, value):
        if isinstance(value, str):
            if len(value) != self.width:
                raise ValueError(f'Value {value} is not the correct width {self.width}')
            for c in value:
                if c not in '01zx':
                    raise ValueError(f'Value {value} contains invalid character {c}')
        elif isinstance(value, int):
            if value < 0:
                if value < -(2**(self.width-1)):
                    raise ValueError(f'Value {value} is out of range for width {self.width}')
                value = 2**self.width + value
                # convert to binary and pad with 1s to width
                value = bin(value)[2:]
                value = '1' * (self.width - len(value)) + value
            elif value >= 2**self.width:
                raise ValueError(f'Value {value} is out of range for width {self.width}')
            else:
                value = bin(value)[2:]
                value = '0' * (self.width - len(value)) + value
        self.value = value

    def get_value(self):
        return self.value

    def print_wire(self):
        print(f"wire [{self.width}-1:0] {self.name};")

    def __str__(self):
        return f'{self.name}'

def unit_test():
    """Unit test for iob_wire"""

    wire0 = iob_wire(name="wire0", width=8)
    wire0.set_value(value=17)
    
    assert wire0.name == "wire0"
    assert wire0.width == 8
    assert wire0.value == '00010001'
    
    wire0.print_wire()
            
# Test the class
if __name__ == "__main__":
    unit_test()
