class iob_val:
    """Class with a binary value supporting x and z"""
    def __init__(self, width=1, value=0):
        if isinstance(value, str):
            if len(value) != width:
                raise ValueError(f'Value {value} is not of width {width}')
            for c in value:
                if c not in '01xz':
                    raise ValueError(f'Value {value} contains invalid character {c}')
        elif isinstance(value, int):
            if value < 0:
                if value < -(2**(width-1)):
                    raise ValueError(f'Value {value} is out of range for width {width}')
                value = 2**width + value
                # convert to binary and pad with 1s to width
                value = bin(value)[2:]
                value = '1' * (width - len(value)) + value
            elif value >= 2**width:
                raise ValueError(f'Value {value} is out of range for width {width}')
            else:
                value = bin(value)[2:]
                value = '0' * (width - len(value)) + value
        self.value = value
        self.width = width

    def __eq__(self, other):
        if isinstance(other, iob_val):
            if self.width != other.width:
                raise ValueError(f'Cannot compare values of different widths {self.width} and {other.width}')
        else:
            raise ValueError(f'Cannot compare iob_val and {type(other)}')
        return self.value == other.value
                
    def __invert__(self):
        result = ''
        for c in self.value:
            if c == '0':
                result += '1'
            elif c == '1':
                result += '0'
            else:
                result += 'x'
        return iob_val(self.width, result)

    def __and__(self, other):
        if isinstance(other, iob_val):
            if self.width != other.width:
                raise ValueError(f'Cannot AND values of different widths {self.width} and {other.width}')
        else:
            raise ValueError(f'Cannot AND iob_val and {type(other)}')
        result = ''
        for i in range(self.width):
            if self.value[i] == '1' and other.value[i] == '1':
                result += '1'
            elif self.value[i] == '0' or other.value[i] == '0':
                result += '0'
            else:
                result += 'x'
        return iob_val(self.width, result)

    def __or__(self, other):
        if isinstance(other, iob_val):
            if self.width != other.width:
                raise ValueError(f'Cannot OR values of different widths {self.width} and {other.width}')
        else:
            raise ValueError(f'Cannot OR iob_val and {type(other)}')
        result = ''
        for i in range(self.width):
            if self.value[i] == '1' or other.value[i] == '1':
                result += '1'
            elif self.value[i] == '0' and other.value[i] == '0':
                result += '0'
            else:
                result += 'x'
        return iob_val(self.width, result)

    def __str__(self):
        return f'{self.width}\'b{self.value}'
    
