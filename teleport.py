import ket

def teleport(alice_msg, alice_aux, bob_aux):
    ket.ctrl(alice_msg, ket.X)(alice_aux)
    ket.H(alice_msg)

    m0 = ket.measure(alice_msg)
    m1 = ket.measure(alice_aux)

    if m1.value == 1:
        ket.X(bob_aux)
    if m0.value == 1:
        ket.Z(bob_aux)

    return bob_aux

def bell(qubits):
    return ket.ctrl(ket.H(qubits[0]), ket.X)(qubits[1])

def message(qubit):
    ket.H(alice)
    ket.Z(alice)

def hello():
    return "World"


if __name__ == '__main__':
    p = ket.Process()

    alice = p.alloc()  # alice = |0⟩
    message(alice)     # alice = |–⟩

    bob = teleport(alice, *bell(p.alloc(2)))  # bob  <- alice

    ket.H(bob)         # bob   = |1⟩
    bob_m = ket.measure(bob)
    print("Expected measure 1, result =", bob_m.value)
