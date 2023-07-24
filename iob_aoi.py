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
        self.port_list = 
            [
                a_i = iob_port("a_i", 1, "input"),
                b_i = iob_port("b_i", 1, "input"),
                c_i = iob_port("c_i", 1, "input"),
                d_i = iob_port("d_i", 1, "input"),
                y_o = iob_port("y_o", 1, "output")
            ]

    def _create_wires(self):
        self.wire_list = 
            [
                aab = iob_wire("aab", 1),
                cad = iob_wire("cad", 1),
                or_res = iob_wire("or_res", 1)
            ]
    def _create_instances(self):
        self.instance_list = 
            [
                and1 = iob_and("and1"),
                and2 = iob_and("and2"),
                or1 = iob_or("or1"),
                inv1 = iob_inv("inv1")
            ]

    def _connect_instances(self):
        and1.port_list[0].connected_to = a_i
        and1.port_list[1].connected_to = b_i
        and1.port_list[2].connected_to = aab
        and2.port_list[0].connected_to = c_i
        and2.port_list[1].connected_to = d_i
        and2.port_list[2].connected_to = cad
        or1.port_list[0].connected_to = aab
        or1.port_list[1].connected_to = cad
        or1.port_list[2].connected_to = or_res
        inv1.port_list[0].connected_to = or_res
        inv1.port_list[1].connected_to = y_o

    def __main__:
        #create build directory

        #call constructor

        #write verilog file
        




