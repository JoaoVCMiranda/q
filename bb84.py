from modules import *

from channels import *
from ket import *

if __name__ == "__main__":

    classicalChannel = ClassicalChannel()
    quantumChannel = QuantumChannel()

    alice = QNode(quantumChannel,classicalChannel)
    bob = QNode(quantumChannel, classicalChannel)

    # Setup
    p = Process()

    # Alice prepares a qubit
    q = p.alloc()

    alice.sendQ(q)
    print(type(quantumChannel.output))
