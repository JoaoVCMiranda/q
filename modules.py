from ket import *
from channels import *

class QNode:
    def __init__(self,quantumC : QuantumChannel , classicalC : ClassicalChannel):
        #self.address = 0 # For routing
        #self.position = (0,0) # For Animating
        self.quantum_port = quantumC
        self.classical_port = classicalC

    def sendQ(self, qubit : Quant):
        self.quantum_port.send(qubit)
    
    def readQ(self):
        self.quantum_port.read()

