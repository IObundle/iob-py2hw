from iob_module import iob_module

class iob_inv(iob_module):
    '''Class for the INV gate module'''
    params = [
        {'name': 'W', 'min_value': 1, 'max_value': 32, 'description': 'Bit width of signals'}
    ]
    param_dict = {'W': 1}
    ports = {
        'i0': {'direction':'input', 'width': 'W', 'description':'Operand 0'},
        'o0': {'direction':'output', 'width': 'W', 'description':'Result'}
    }
    assigns = {'o0':'~i0'}
    descriprion = "General bit-wise INV gate with default 1-bit operands and result"
