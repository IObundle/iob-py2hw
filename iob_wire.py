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
        # if value is boolean convert to string and check self.width = 1
        elif isinstance(value, bool):
            if self.width != 1:
                raise ValueError(f'Value {value} is not the correct width {self.width}')
            value = '1' if value else '0'
        self.value = value

    def get_value(self):
        return self.value

    def print_verilog(self):
        print(f"  wire [{self.width}-1:0] {self.name};")

    # Comparison operators
    def __eq__(self, other):
        if isinstance(other, iob_wire):
            if self.width != other.width:
                raise ValueError(f'Cannot compare wires of different widths {self.width} and {other.width}')
        else:
            raise ValueError(f'Cannot compare iob_wire and {type(other)}')
        return self.get_value() == other.get_value()

    # Bitwise operators
    def __invert__(self):
        result = ''
        for c in self.get_value():
            if c == '0':
                result += '1'
            elif c == '1':
                result += '0'
            else:
                result += 'x'
        return result

    def __and__(self, other):
        if isinstance(other, iob_wire):
            if self.width != other.width:
                raise ValueError(f'Cannot AND wires of different widths {self.width} and {other.width}')
        else:
            raise ValueError(f'Cannot AND iob_wire and {type(other)}')
        result = ''
        for i in range(self.width):
            if self.get_value()[i] == '1' and other.get_value()[i] == '1':
                result += '1'
            elif self.get_value()[i] == '0' or other.get_value()[i] == '0':
                result += '0'
            else:
                result += 'x'
        return result

    def __or__(self, other):
        if isinstance(other, iob_wire):
            if self.width != other.width:
                raise ValueError(f'Cannot OR wires of different widths {self.width} and {other.width}')
        else:
            raise ValueError(f'Cannot OR iob_wire and {type(other)}')
        result = ''
        for i in range(self.width):
            if self.get_value()[i] == '1' or other.get_value()[i] == '1':
                result += '1'
            elif self.get_value()[i] == '0' and other.get_value()[i] == '0':
                result += '0'
            else:
                result += 'x'
        return result

    def __str__(self):
        return f'{self.name}'

def unit_test():
    """Unit test for iob_wire"""

    wire0 = iob_wire(name="wire0", width=8)
    wire0.set_value(value=17)
    
    assert wire0.name == "wire0"
    assert wire0.width == 8
    assert wire0.value == '00010001'
    
    wire0.print_verilog()
            
# Test the class
if __name__ == "__main__":
    unit_test()
