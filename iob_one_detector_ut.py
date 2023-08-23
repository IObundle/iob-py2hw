from iob_one_detector import iob_one_detector
from iob_wire import iob_wire

def unit_test():
    # Create 4 wires 1-bit wide
    w0 = iob_wire(name='w0', width=1)
    w1 = iob_wire(name='w1', width=1)
    w2 = iob_wire(name='w2', width=1)
    w3 = iob_wire(name='w3', width=1)

    od0 = iob_one_detector.create(
        instance_name = 'od0',
        description = "This is a test module",
        param_dict = {'W': 1},
        port_map = {
            'i0': w0,
            'en': w1,
            'o0': w2,
            'en_next': w3
        }
    )

    od0.print_verilog_module()
    od0.print_verilog_module_inst()

if __name__ == "__main__":
    unit_test()
