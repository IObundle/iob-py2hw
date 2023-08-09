from iob_port import iob_port
from iob_wire import iob_wire
from iob_assign import iob_assign

class iob_bassign(iob_assign):
    '''Class for the binary assign statement'''
    def __init__(self, name, operator, operand0, operand1, result, description):
        super().__init__(name, description)
        self.operator = operator
        self.operand0 = operand0
        self.operand1 = operand1
        self.result = result

    def print_verilog(self):
        print(f'assign {self.result.name} = {self.operand0.name}{self.operator}{self.operand1.name};')

def unit_test():
    '''Unit test for iob_assign'''
    # Create 3 wire
    w0 = iob_wire(name='w0', width=8, value=0)
    w1 = iob_wire(name='w1', width=8, value=0)
    w2 = iob_wire(name='w2', width=8, value=0)

    # Create operator
    operator = '&'

    # Create assign
    assign0 = iob_bassign(
        name='assign0',
        operator=operator,
        operand0=w1,
        operand1=w2,
        result=w0,
        description='Assign w1&w2 to w0'
    )

    assert assign0.name == 'assign0'
    assert assign0.operator == '&'
    assert assign0.operand0 == w1
    assert assign0.operand1 == w2
    assert assign0.result == w0
    assert assign0.description == 'Assign w1&w2 to w0'

    assign0.print_verilog()

if __name__ == '__main__':
    unit_test()
