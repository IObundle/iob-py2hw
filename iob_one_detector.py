from iob_module import iob_module

class iob_one_detector(iob_module):
    """Class for the one detector module"""
    ports = {
        'i0': {'direction':'input', 'width': 'W', 'description':'Operand 0'},
        'en': {'direction':'input', 'width': 'W', 'description':'Enable'},
        'o0': {'direction':'output', 'width': 'W', 'description':'Result'},
        'en_next': {'direction':'output', 'width': 'W', 'description':'Next enable'}
    }
    assigns = {
        'o0':'i0 & en',
        'en_next':'en & ~i0'
    }
    description = "One detector module"
