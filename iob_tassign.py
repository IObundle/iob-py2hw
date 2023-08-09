from iob_port import iob_port
from iob_wire import iob_wire
from iob_assign import iob_assign

class iob_tassign(iob_assign):
    '''Class for the ternary assign statement'''
    def __init__(self, name, operand0, operand1, operand2, result, description):
        super().__init__(name, description)
        self.operand0 = operand0
        self.operand1 = operand1
        self.operand2 = operand2
        self.result = result

    def print_verilog(self):
        print(f'assign {self.result.name} = {self.operand0.name} ? {self.operand1.name} : {self.operand2.name};')

def unit_test():
    '''Unit test for iob_assign'''
    # Create 4 wire
    w0 = iob_wire(name='w0', width=8, value=0)
    w1 = iob_wire(name='w1', width=1, value=0)
    w2 = iob_wire(name='w2', width=8, value=0)
    w3 = iob_wire(name='w3', width=8, value=0)

    # Create assign
    assign0 = iob_tassign(
        name='assign0',
        operand0=w1,
        operand1=w2,
        operand2=w3,
        result=w0,
        description='Assign w2 to w0 if w1 is true, otherwise assign w3 to w0'
    )

    assert assign0.name == 'assign0'
    assert assign0.operand0 == w1
    assert assign0.operand1 == w2
    assert assign0.operand2 == w3
    assert assign0.result == w0
    assert assign0.description == 'Assign w2 to w0 if w1 is true, otherwise assign w3 to w0'

    assign0.print_verilog()

if __name__ == '__main__':
    unit_test()
