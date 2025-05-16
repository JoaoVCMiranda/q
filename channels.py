import random

from ket import *

class ClassicalChannel:
    def __init__(self):
        #self.cost = 0 
        self.distance = 0
        self.speed_of_light = 208189.206944 # km/s
        self.error_rate = 0

class QuantumChannel:
    def __init__(self):
        self.cost = 0
        self.distance = 0
        self.speed_of_light = 208189.206944 # km/s
        self.error_rate = .5
        self.x_error_proportion_rate = 1
        self.y_error_proportion_rate = 1
        self.z_error_proportion_rate = 1
        self.input = None
        self.output = None
    
    def send(self, qubit : Quant):
        self.input = qubit
        self.output = self.transmit(qubit)
    
    def transmit(self, qubit : Quant):
        return qubit if self.error_rate < random.random() else None





