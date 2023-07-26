import copy

from iob_module import iob_module
from iob_port import iob_port
from named_list import named_list

class iob_or(iob_module):
    """Class to represent an or gate in an iob module"""
    port_list = named_list(
        [
            iob_port("a_i", 1, "input"),
            iob_port("b_i", 1, "input"),
            iob_port("y_o", 1, "output")
        ]
    )
   
    def __init__(self, name=""):
        self.name = name
        self.port_map = copy.deepcopy(self.port_list)
        for port in self.port_map:
            port.connected_to = None
