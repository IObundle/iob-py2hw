import os
import copy

from iob_module import iob_module
from named_list import named_list

from iob_port import iob_port
from iob_wire import iob_wire
from iob_and import iob_and
from iob_or import iob_or
from iob_inv import iob_inv

class iob_aoi(iob_module):
    isPrimitive = False

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
        self.port_map = named_list()
        create_input_port("a_i", 1)
        create_input_port("b_i", 1)
        create_input_port("c_i", 1)
        create_input_port("d_i", 1)
        create_output_port("y_o", 1)
        
        self.wire_list = named_list()
        create_wire("aab", 1)
        create_wire("cad", 1)
        create_wire("or_res", 1)

        self.instance_list = named_list()
        create_module(iob_and, "and1", {"a_i": "a_i", "b_i": "b_i", "y_o": "aab"})
        create_module(iob_and, "and2", {"a_i": "c_i", "b_i": "d_i", "y_o": "cad"})
        create_module(iob_or, "or1", {"a_i": "aab", "b_i": "cad", "y_o": "or_res"})
        create_module(iob_inv, "inv1", {"a_i": "or_res", "y_o": "y_o"})

    @classmethod
    def _create_ports(cls):
        cls.port_list = named_list(
            [
                iob_port("a_i", 1, "input"),
                iob_port("b_i", 1, "input"),
                iob_port("c_i", 1, "input"),
                iob_port("d_i", 1, "input"),
                iob_port("y_o", 1, "output")
            ]
        )

    @classmethod
    def _create_wires(cls):
        cls.wire_list = named_list(
            [
                iob_wire("a_i", 1),
                iob_wire("b_i", 1),
                iob_wire("c_i", 1),
                iob_wire("d_i", 1),
                iob_wire("aab", 1),
                iob_wire("cad", 1),
                iob_wire("or_res", 1),
                iob_wire("y_o", 1)
            ]
        )
                
    @classmethod
    def _create_instances(cls):
        cls.instance_list = named_list(
            [
                create_module(iob_and, "and1", {"a_i": "a_i", "b_i": "b_i", "y_o": "aab"}),
                create_module(iob_and, "and2", {"a_i": "c_i", "b_i": "d_i", "y_o": "cad"}),
                create_module(iob_or, "or1", {"a_i": "aab", "b_i": "cad", "y_o": "or_res"}),
                create_module(iob_inv, "inv1", {"a_i": "or_res", "y_o": "y_o"})
            ]
        )

    def create_input_port(self, name, bit_width):
        p = iob_port(name, "input")
        self.port_map.append(p)
        return p

    def create_output_port(self, name, bit_width):
        p = iob_port(name, "output")
        p.connect(self.create_wire(name, bit_width))
        self.port_map.append(p)
        return p
        
    def create_wire(self, name, bit_width):
        w = iob_wire(name, bit_width)
        self.wire_list.append(w)
        return w

    def create_module(self, module, name, ports):
        """Create an instance of a module and connect it to this module"""
        inst = module(name)
        for port in ports:
            inst.port_map[port].connect(self.wire_list[ports[port]])
        return inst

if __name__ == "__main__":        
        #create build directory
        build_dir = "build"
        if not os.path.exists(build_dir):
            os.makedirs(build_dir)

        #call constructor
        aoi = iob_aoi("aoi1")
        #print object hierarchy
        print(aoi.name)
        for port in aoi.port_map:
            print(port.name)
        for wire in aoi.wire_list:
            print(wire.name)
        for instance in aoi.instance_list:
            print(instance.name)
        #write verilog file
