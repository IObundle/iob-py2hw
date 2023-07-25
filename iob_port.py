from iob_wire import iob_wire

class iob_port():
    """Class to represent a port in an iob module"""
        
    def __init__(self, name="", bit_width=1, direction="input"):
        self.name = name
        self.direction = direction
        self.wire = iob_wire(name, bit_width)
