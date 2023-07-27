from iob_module import iob_module
from iob_param import iob_param
from iob_port import iob_port
from iob_wire import iob_wire


class iob_and(iob_module):
    '''Class for the AND gate module'''
    def __init__(self, name, port_matrix, param_matrix = []):
        '''Constructor for the AND gate module'''
        self.name = name
        self.port_list = []
        for i in range(len(port_matrix)):
            self.port_list.append(
                iob_port(
                    port_matrix[i][1],
                    port_matrix[i][2],
                    port_matrix[i][3],
                    port_matrix[i][0])
            )
        self.param_list = []
        for i in range(len(param_matrix)):
            self.param_list.append(
                iob_param(
                    param_matrix[i][0],
                    param_matrix[i][1],
                    param_matrix[i][2])
            )

        super().__init__(name, self.port_list, self.param_list)
            

#Test
if __name__ == '__main__':

    a = iob_and(
        name = 'and0',
        port_matrix = [
            ['input', 'i0', 'W', 'a'],
            ['input', 'i1', 'W', 'b'],
            ['output', 'o0', 'W', 'c']
        ],
        param_matrix = [
            ['W', 32, 1]
        ]
    )
    
    a.port_list[0].connect_wire(iob_wire('a', 4))
    a.port_list[1].connect_wire(iob_wire('b', 4))
    a.port_list[2].connect_wire(iob_wire('c', 4))
    
    a.print_verilog_module(a)
    a.print_verilog_module_inst(a)


