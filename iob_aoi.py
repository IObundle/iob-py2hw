from iob_module import iob_module
from iob_param import iob_param
from iob_port import iob_port
from iob_wire import iob_wire
from iob_and import iob_and
from iob_or import iob_or
from iob_inv import iob_inv

class iob_aoi(iob_module):
    """AOI module class"""

    def __init__(self, name, port_matrix):
        """AOI module constructor"""

        # Create wire list with 3 1bit wires
        wire_list = [
            iob_wire(f"{name}_and0_out", 1, 1),
            iob_wire(f"{name}_and1_out", 1, 1),
            iob_wire(f"{name}_or_out", 1, 1)
            ]

        # Create port list from port matrix
        port_list = []
        for i in range(len(port_matrix)):
            port_list.append(
                iob_port(
                    port_matrix[i][1],
                    port_matrix[i][2],
                    port_matrix[i][0])
            )
            port_list[i].connect(port_matrix[i][3])
        
        and0 = iob_and(
            name = f"{name}_and0",
            port_matrix = [
                ['input', 'i0', 2, port_list[0].value],
                ['output', 'o0', 1, wire_list[0]]
            ],
            param_matrix = [
                ['W', 32, 1],
                ['N', 32, 2]
            ]
        )

        and1 = iob_and(
            name = f"{name}_and1",
            port_matrix = [
                ['input', 'i0', 2, port_list[1].value],
                ['output', 'o0', 1, wire_list[1]]
            ],
            param_matrix = [
                ['W', 32, 1],
                ['N', 32, 2]
            ]
        )
                
        or0 = iob_or(
            name = f"{name}_or0",
            port_matrix = [
                ['input', 'i0', 1, wire_list[0]],
                ['input', 'i0', 1, wire_list[1]],
                ['output', 'o0', 1, wire_list[2]]
            ],
            param_matrix = [
                ['W', 32, 1],
                ['N', 32, 2]
            ]
        )
        
        inv0 = iob_inv(
            name = f"{name}_inv0",
            port_matrix = [
                ['input', 'i0', 1, wire_list[2]],
                ['output', 'o0', 1, port_list[2].value]
            ],
            param_matrix = [
                ['W', 32, 1]
            ]
        )

        # Create instance list
        instance_list = [and0, and1, or0, inv0]
        
        # Call super class constructor
        super().__init__(name=name, port_list=port_list, wire_list=wire_list, inst_list=instance_list)

def unit_test():
    '''Unit test for AOI module'''

    # Create 3 wires
    wire0 = iob_wire("wire0", 2, 1)
    wire1 = iob_wire("wire1", 2, 1)
    wire4 = iob_wire("wire4", 1, 1)

    # Create aoi0 module
    aoi0 = iob_aoi(
        name = "aoi0",
        port_matrix = [
            ['input', 'i0', 2, wire0],
            ['input', 'i1', 2, wire1],
            ['output', 'o0', 1, wire4]
        ]
    )
    
    # Print the module
    aoi0.print_verilog_module()
    # Print instance
    aoi0.print_verilog_module_inst()

if __name__ == "__main__":
    unit_test()
