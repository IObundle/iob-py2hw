from iob_datum import iob_datum
from iob_wire import iob_wire

class iob_port(iob_datum):
    """Class to represent a port in an iob module"""

    def __init__(self, name, width,  value, direction = "input"):
        super().__init__(name, width)
        self.direction = direction
        self.wire = None
        # test if direction is 'input', 'output', 'inout'; exit with error otherwise
        if direction not in ["input", "output", "inout"]:
            print(f"Error: Direction must be 'input', 'output', or 'inout'.")
            exit(1)
        
    def print_port(self, comma=True):
        if comma:
            print(f"      {self.direction} [{self.width}-1:0] {self.name},")
        else:
            print(f"      {self.direction} [{self.width}-1:0] {self.name}")

        
    def print_port_assign(self, comma=True):
        if self.wire == None:
            print(f"Error: Port {self.name} is not connected to a wire.")
            exit(1)
        if comma:
            print(f"      .{self.name}({self.wire.name}),")
        else:
            print(f"      .{self.name}({self.wire.name})")

    def connect_wire(self, wire):
        if self.width != wire.width:
            print(f"Error: Wire width ({wire.width}) does not match port width ({port.width}).")
            exit(1)
        else self.wire = wire


# Test code
if __name__ == "__main__":

    a = iob_wire("a", 4, 8)
    b = iob_wire("b", 4, 8)
    c = iob_wire("c", 4, 8)
    
    port1 = iob_port("port1", 4, a, "input")
    port2 = iob_port("port2", 4, b, "output")
    port3 = iob_port("port3", 4, c, "inout")
    port1.print_port()
    port2.print_port()
    port3.print_port()

    port1.connect_wire(a)
    port2.connect_wire(b)
    port3.connect_wire(c)

    port1.print_port_assign(port1.wire)
    port2.print_port_assign(port2.wire)
    port3.print_port_assign(port3.wire)
