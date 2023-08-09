from iob_port import iob_port
from iob_wire import iob_wire
from iob_assign import iob_assign

class iob_uassign(iob_assign):
    '''Class for the assign statement'''
    def __init__(self, name, operator, operand, result, description):
        super().__init__(name, operator, result, description)
        self.operand = operand

    def print_verilog(self):
        print(f'assign {self.result.name} = {self.operator}{self.operand};')

def unit_test():
    '''Unit test for iob_assign'''
    # Create 2 wire
    w0 = iob_wire(name='w0', width=8, value=0)
    w1 = iob_wire(name='w1', width=8, value=0)

    # Create operator
    operator = '!'

    # Create assign
    assign0 = iob_uassign(
        name='assign0',
        operator=operator,
        operand='w1',
        result=w0,
        description='Assign !w1 to w0'
    )

    assign0.print_verilog()

if __name__ == '__main__':
    unit_test()
