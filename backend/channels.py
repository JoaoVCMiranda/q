import random

from ket import *
from modulos import *
import numpy as np

class ClassicalChannel:
    def __init__(self):
        #self.cost = 0
        self.distance = 0
        self.speed_of_light = 208189.206944 # km/s
        self.error_rate = 0

class QuantumChannel:
    def __init__(self, **kwargs):
        self.cost = kwargs.get('cost', 0)
        self.distance = kwargs.get('distance', 0) # km
        self.speed_of_light = kwargs.get('speed_of_light', 208189.206944)  # km/s
        self.loss_rate = kwargs.get('loss_rate', 0) # per km
        self.error_rate = kwargs.get('error_rate', 0) # per km
        self.error_proportion_rate = [kwargs.get('x_error_proportion_rate', 1) ,kwargs.get('y_error_proportion_rate', 1), kwargs.get('z_error_proportion_rate', 1)]
        self.input = None
        self.output = None
        self.nodes = [None, None]

    def send(self, qubit : Quant):
        self.input = qubit
        self.output = self.transmit(qubit)

    def channel_error(self, qubit):
        orientation = ["X", "Y", "Z"]
        if self.error_rate > random.random():
            orientation = random.choices(orientation, self.error_proportion_rate)[0]
            #print("Error!")
            #print(orientation)
        return qubit

    def transmit(self, qubit : Quant):
        return self.channel_error(qubit) if self.loss_rate*self.distance < random.random() else None

    def subscribe(self,node):
        for i,n in enumerate(self.nodes):
            if n == None:
                self.nodes[i] = node
                break

    def read(self, node):
        if (node == self.nodes[0]):
            return self.input
        if (node == self.nodes[1]):
            return self.output
        return None
    def insert_axis_noise( ket: Quant, qubit_index: int, axis: str, noise_type: str = "bit_flip_phase_flip", probability: float = 0.05, max_angle: float = np.pi / 10) -> Quant:

        if not 0 <= qubit_index < ket.num_qubits:
            raise ValueError(f"qubit_index {qubit_index} is out of bounds for Ket with {ket.num_qubits} qubits.")
        if not 0 <= probability <= 1:
            raise ValueError("Probability must be between 0 and 1.")
        if max_angle < 0:
            raise ValueError("max_angle must be non-negative.")
        if axis.upper() not in ['X', 'Y', 'Z']:
            raise ValueError("Axis must be 'X', 'Y', or 'Z'.")

        noisy_ket = ket.copy()  # Create a copy to avoid modifying the original Ket
        qubit_obj = Qubit(qubit_index)

        axis_upper = axis.upper()

        if noise_type == "random_rotation":
            random_angle = np.random.uniform(-max_angle, max_angle)
            if axis_upper == 'X':
                noisy_ket.apply_operator(RX(qubit_obj, random_angle))
                print(f"Applied RX({random_angle:.4f}) to qubit {qubit_index} (random X-rotation noise).")
            elif axis_upper == 'Y':
                noisy_ket.apply_operator(RY(qubit_obj, random_angle))
                print(f"Applied RY({random_angle:.4f}) to qubit {qubit_index} (random Y-rotation noise).")
            elif axis_upper == 'Z':
                noisy_ket.apply_operator(RZ(qubit_obj, random_angle))
                print(f"Applied RZ({random_angle:.4f}) to qubit {qubit_index} (random Z-rotation noise).")
        elif noise_type in ["bit_flip", "bit_flip_phase_flip", "phase_flip"]:
            if np.random.rand() < probability:
                if axis_upper == 'X' and noise_type == "bit_flip":
                    noisy_ket.apply_operator(X(qubit_obj))
                    print(f"Applied X gate to qubit {qubit_index} (bit-flip noise).")
                elif axis_upper == 'Y' and noise_type == "bit_flip_phase_flip":
                    noisy_ket.apply_operator(Y(qubit_obj))
                    print(f"Applied Y gate to qubit {qubit_index} (bit-flip and phase-flip noise).")
                elif axis_upper == 'Z' and noise_type == "phase_flip":
                    noisy_ket.apply_operator(Z(qubit_obj))
                    print(f"Applied Z gate to qubit {qubit_index} (phase-flip noise).")
                else:
                    raise ValueError(f"Invalid noise_type '{noise_type}' for axis '{axis_upper}'.")
            else:
                print(f"Probabilistic {noise_type} on {axis_upper}-axis for qubit {qubit_index} did not occur.")
        else:
            raise ValueError(f"Invalid noise_type '{noise_type}'. "
                            "Choose 'random_rotation', 'bit_flip' (for X), "
                            "'bit_flip_phase_flip' (for Y), or 'phase_flip' (for Z).")

        return noisy_ket
# Frederick Roassats
#   Paolo Fitpaudi *
#       Rule set que descreva o protocolo
#       Sistema de sinais de acontecimentos & em sinais
#       Exportar o csv
#       "Consume"
#       setAllocated(false ) -> Jogado fora
#   Rodar dentro do devcontainer
#   localhost:6090
#   E# de memórias na memória
#   O tempo dos photons se dá entre o menor dos dois pontos na memórias
