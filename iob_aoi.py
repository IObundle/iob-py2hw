import os

from iob_module import iob_module

from iob_port import iob_port
from iob_wire import iob_wire

class iob_aoi(iob_module):
    name = "iob_aoi"

    def __init__(self, name=""):
        self.name = name
        self._create_ports()
        self._create_wires()
        self._create_instances()
        self._connect_instances()

    def _create_ports(self):
        self.port_list = {}
        self.port_list["a_i"] = iob_port("a_i", 1, "input")
        self.port_list["b_i"] = iob_port("b_i", 1, "input")
        self.port_list["c_i"] = iob_port("c_i", 1, "input")
        self.port_list["d_i"] = iob_port("d_i", 1, "input")
        self.port_list["y_o"] = iob_port("y_o", 1, "output")

    def _create_wires(self):
        self.wire_list = {}
        self.wire_list["aab"] = iob_wire("aab", 1)
        self.wire_list["cad"] = iob_wire("cad", 1)
        self.wire_list["or_res"] = iob_wire("or_res", 1)
                
    def _create_instances(self):
        self.instance_list = {}
        self.instance_list["and1"] = iob_and("and1")
        self.instance_list["and2"] = iob_and("and2")
        self.instance_list["or1"] = iob_or("or1")
        self.instance_list["inv1"] = iob_inv("inv1")

    def _connect_instances(self):
        self.instance_list["and1"].port_list["a_i"].connected_to = self.port_list["a_i"]
        self.instance_list["and1"].port_list["b_i"].connected_to = self.port_list["b_i"]
        self.instance_list["and1"].port_list["y_o"].connected_to = self.wire_list["aab"]

        self.instance_list["and2"].port_list["a_i"].connected_to = self.port_list["c_i"]
        self.instance_list["and2"].port_list["b_i"].connected_to = self.port_list["d_i"]
        self.instance_list["and2"].port_list["y_o"].connected_to = self.wire_list["cad"]

        self.instance_list["or1"].port_list["a_i"].connected_to = self.wire_list["aab"]
        self.instance_list["or1"].port_list["b_i"].connected_to = self.wire_list["cad"]
        self.instance_list["or1"].port_list["y_o"].connected_to = self.wire_list["or_res"]

        self.instance_list["inv1"].port_list["a_i"].connected_to = self.wire_list["or_res"]
        self.instance_list["inv1"].port_list["y_o"].connected_to = self.port_list["y_o"]

    def __main__:
        #create build directory

        #call constructor

        #write verilog file
        




