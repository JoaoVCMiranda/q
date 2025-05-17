from modulos import *

from channels import *
from ket import *

def exec(n_qubits, distance, loss_rate):
    classicalChannel = ClassicalChannel()
    quantumChannel = QuantumChannel(distance=distance, loss_rate=loss_rate, error_rate=0.1)

    alice = QNode(quantumChannel,classicalChannel)
    bob = QNode(quantumChannel, classicalChannel)

    # Setup
    p = Process()
    n_qubits = 33
    # Alice prepares sequence
    alice_seq =[ 1 if 0.5 < random.random() else 0 for x in range(n_qubits)]
    bob_seq = []

    for b in alice_seq:
        q = p.alloc()
        if b:
            X(q)

        alice.send_q(q)
        bob_seq.append(bob.read_q())

    #print("------------------")
    #print(n_qubits, distance, loss_rate)
    #print(alice_seq)
    #print(bob_seq)
    return (alice_seq, bob_seq)

if __name__ == "__main__":
    exec()
