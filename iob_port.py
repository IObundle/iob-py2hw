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

def unit_test():
    """Unit test for iob_port"""
    
    # Create 3 wires
    wire0 = iob_wire(name="wire0", width=8)
    wire0.set_value(value=17)
    wire1 = iob_wire(name="wire1", width=8)
    wire1.set_value(value=42)
    wire2 = iob_wire(name="wire2", width=8)
    wire2.set_value(value=0)

    # Create 3 ports
    port0 = iob_port(name="port0", width=8, direction="input")
    port0.connect(wire0)
    port1 = iob_port(name="port1", width=8, direction="output")
    port1.connect(wire1)
    port2 = iob_port(name="port2", width=8, direction="inout")
    port2.connect(wire2)

    # Check if the ports are correct

    assert port0.name == "port0"
    assert port0.width == 8
    assert port0.value == wire0
    assert port0.direction == "input"
    assert port0.get_value() == '00010001'
    port0.set_value(value=18)
    assert port0.get_value() == '00010010'
    assert wire0.get_value() == '00010010'

    assert port1.name == "port1"
    assert port1.width == 8
    assert port1.value == wire1
    assert port1.direction == "output"
    assert port1.get_value() == '00101010'
    port1.set_value(value=43)
    assert port1.get_value() == '00101011'
    assert wire1.get_value() == '00101011'

    assert port2.name == "port2"
    assert port2.width == 8
    assert port2.value == wire2
    assert port2.direction == "inout"
    assert port2.get_value() == '00000000'
    port2.set_value(value=44)
    assert port2.get_value() == '00101100'
    assert wire2.get_value() == '00101100'

    assert (port0 == port1) == False
    assert (port1 == port1) == True
    assert (port1 & port2) == '00101000'

    port0.print_port()
    port1.print_port()
    port2.print_port()

    port0.print_port_assign()
    port1.print_port_assign()
    port2.print_port_assign()
    
# Test code
if __name__ == "__main__":
    unit_test()
