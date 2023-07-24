from iob_wire import io_wire

class iob_port(iob_wire):
    """Class to represent a port in an iob module"""
        
        def __init__(self, name="", bit_width=1, direction="input"):
            iob_wire.__init__(self, name, bit_width)
            self.direction = direction
            self.connected_to = None
