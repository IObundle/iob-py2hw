from iob_module import iob_module

class iob_and(iob_module):
    '''Class for the AND gate module'''
    params = [
        {'name': 'W', 'min_value': 1, 'max_value': 32, 'description': 'Bit width of signals'}
    ]
    param_dict = {'W': 1}
    ports = {
        'i0': {'direction':'input', 'width': 'W', 'description':'Operand 0'},
        'i1': {'direction':'input', 'width': 'W', 'description':'Operand 1'},
        'o0': {'direction':'output', 'width': 'W', 'description':'Result'}
    }
    assigns = {'o0':'i0 & i1'}
    descriprion = "General bit-wise AND gate with default 1-bit operands and result"
