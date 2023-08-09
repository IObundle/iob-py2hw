from iob_port import iob_port
from iob_wire import iob_wire

class iob_assign():
    '''Class for the assign statement'''
    def __init__(self, name, result, description):
        self.name = name
        self.result = result
        self.description = description

    def print_verilog(self):
        print(f'assign {self.result.name} =;')


def unit_test():
    '''Unit test for iob_assign'''
    # Create 1 wire
    w0 = iob_wire(name='w0', width=8, value=0)

    # Create assign
    assign0 = iob_assign(
        name='assign0',
        result=w0,
        description='Assign something to w0'
    )

    assign0.print_verilog()

if __name__ == '__main__':
    unit_test()
