from iob_wire import iob_wire

class iob_port():
    """Class to represent a port in an iob module"""
        
    def __init__(self, name="", direction="input"):
        self.name = name
        self.direction = direction
        self.wire = None

    def connect(self, wire):
        self.wire = wire
