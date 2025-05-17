from ket import *
from channels import *

class QNode:
    def __init__(self,quantumC : QuantumChannel , classicalC : ClassicalChannel):
        #self.address = 0 # For routing
        #self.position = (0,0) # For Animating
        quantumC.subscribe(self)
        self.quantum_port = quantumC
        self.classical_port = classicalC

    def send_q(self, qubit : Quant):
        self.quantum_port.send(qubit)
    
    def read_q(self):
        if self.quantum_port.read(self) == None:
            return None
        return measure(self.quantum_port.read(self)).value

