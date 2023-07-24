import os
import copy

from iob_module import iob_module
from named_list import named_list

from iob_port import iob_port
from iob_wire import iob_wire

class iob_aoi(iob_module):
    name = "iob_aoi"

    @classmethod
    def init_atributes(cls):
        """Initialize class attributes for this class"""
        super().init_atributes()
        cls._create_ports()
        cls._create_wires()
        cls._create_instances()
        cls._connect_instances()
    
    def __init__(self, name=""):
        self.name = name
        #port_map is used to connect external wires to this module
        self.port_map = copy.deepcopy(self.port_list)
        for port in self.port_map.values():
            port.connected_to = None
        self.wire_list = copy.deepcopy(self.wire_list)
        self.instance_list = copy.deepcopy(self.instance_list)
        self._connect_instances()

    @classmethod
    def _create_ports(cls):
        cls.port_list = named_list
            ([
                iob_port("a_i", 1, "input"),
                iob_port("b_i", 1, "input"),
                iob_port("c_i", 1, "input"),
                iob_port("d_i", 1, "input"),
                iob_port("y_o", 1, "output")
            ])

    @classmethod
    def _create_wires(cls):
        cls.wire_list = named_list
            ([
                iob_wire("aab", 1),
                iob_wire("cad", 1),
                iob_wire("or_res", 1)
            ])
                
    @classmethod
    def _create_instances(cls):
        cls.instance_list = named_list
            ([
                iob_and("and1"),
                iob_and("and2"),
                iob_or("or1"),
                iob_inv("inv1")
            ])

    @classmethod
    def _connect_instances(cls):
        cls.instance_list["and1"].port_map["a_i"].connected_to = cls.port_list["a_i"]
        cls.instance_list["and1"].port_map["b_i"].connected_to = cls.port_list["b_i"]
        cls.instance_list["and1"].port_map["y_o"].connected_to = cls.wire_list["aab"]

        cls.instance_list["and2"].port_map["a_i"].connected_to = cls.port_list["c_i"]
        cls.instance_list["and2"].port_map["b_i"].connected_to = cls.port_list["d_i"]
        cls.instance_list["and2"].port_map["y_o"].connected_to = cls.wire_list["cad"]

        cls.instance_list["or1"].port_map["a_i"].connected_to = cls.wire_list["aab"]
        cls.instance_list["or1"].port_map["b_i"].connected_to = cls.wire_list["cad"]
        cls.instance_list["or1"].port_map["y_o"].connected_to = cls.wire_list["or_res"]

        cls.instance_list["inv1"].port_map["a_i"].connected_to = cls.wire_list["or_res"]
        cls.instance_list["inv1"].port_map["y_o"].connected_to = cls.port_list["y_o"]

if __name__ == "__main__":        
        #create build directory

        #call constructor

        #write verilog file
        




