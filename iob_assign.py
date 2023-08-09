from iob_port import iob_port
from iob_wire import iob_wire

class iob_assign():
    '''Class for the assign statement'''
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def print_verilog(self):
        #To be implemented by the subclass
        pass


def unit_test():
    '''Unit test for iob_assign'''
    # Create assign
    assign0 = iob_assign(
        name='assign0',
        description='Assign instance'
    )

    assert assign0.name == 'assign0'
    assert assign0.description == 'Assign instance'

    assign0.print_verilog()

if __name__ == '__main__':
    unit_test()
