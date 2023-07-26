import os

import iob_port
import iob_wire

class iob_module:
    name = ""
    is_primitive = True
    
    def _create_ports(self):
        """To be implemented by subclass"""
        pass
        
    def _create_wires(self):
        """To be implemented by subclass"""
        pass

    def _create_instances(self):
        """To be implemented by subclass"""
        pass

    def _connect_instances(self):
        """To be implemented by subclass"""
        pass
