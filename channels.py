import random

from ket import *
from modulos import *

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
