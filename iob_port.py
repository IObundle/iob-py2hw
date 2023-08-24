from iob_wire import iob_wire

class iob_port(iob_wire):
    """Class to represent a port in an iob module"""

    def __init__(self, name, width, direction = "input"):
        super().__init__(name=name, width=width)
        if direction not in ["input", "output", "inout"]:
            print(f"Error: Direction must be 'input', 'output', or 'inout'.")
            exit(1)
        self.direction = direction

    def connect(self, value):
        """Connect a wire to the port"""
        if not isinstance(value, (iob_wire, iob_port)):
            raise ValueError(f"Error: Port {self.name} can only be connected to a wire or port.")
        if value.width != self.width:
            print(f"Error: Port {self.name} width ({self.width}) does not match wire {value.name} width ({value.width}).")
            exit(1)
        self.value = value

    def set_value(self, value):
        self.wire().set_value(value)

    def get_value(self):
        return self.wire().get_value()

    def wire(self):
        """Return the wire connected to the port"""
        return self.value
        
    def print_port(self, comma=True):
        if comma:
            print(f"      {self.direction} [{self.width}-1:0] {self.name},")
        else:
            print(f"      {self.direction} [{self.width}-1:0] {self.name}")

        
    def print_port_assign(self, comma=True):
        if not isinstance(self.value, (iob_wire, iob_port)):
            print(f"Error: Port {self.name} is not connected.")
            exit(1)
        if comma:
            print(f"      .{self.name}({self.value.name}),")
        else:
            print(f"      .{self.name}({self.value.name})")
