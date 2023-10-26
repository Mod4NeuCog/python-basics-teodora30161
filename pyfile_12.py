#Exercise 1: Taxonomy of neuron models

#Making a NeuronalCell class
class NeuronalCell:
    #Constructor with attributes for the membrane potential and the type
    def __init__(self, V_membrane, type):
        self.V_membrane = V_membrane
        self.type = type

#PyramidalNeuron is a subclass of NeuronalCell:
class PyramidalNeuron(NeuronalCell):
    #I reuse the constructor from NeuronalCell
    def __init__(self, V_membrane, type):
        super().__init__(V_membrane, type)

#Another subclass:
class OvoidNeuron(NeuronalCell):
    def __init__(self, V_membrane, type):
        super().__init(V_membrane, type)

#Exercise 2: Instantiation and interaction between neurons

#I remake the classes, adding methods to send and receive spikes:
class NeuronalCell:
    def __init__(self, V_membrane, type):
        self.V_membrane = V_membrane
        self.type = type
    def receiveSpike(self, spike):
        self.V_membrane = self.V_membrane + spike
    def sendSpike(self):
        if(self.V_membrane > -65):
            return 5
        else:
            return 0

class PyramidalNeuron(NeuronalCell):
    def __init__(self, V_membrane, type):
        super().__init__(V_membrane, type)

class OvoidNeuron(NeuronalCell):
    def __init__(self, V_membrane, type):
        super().__init__(V_membrane, type)

#I instantiate two different neurons
n1 = PyramidalNeuron(-75, "a")
n2 = OvoidNeuron(-80, "b")

#I give n1 a spike of 20 mV to make it go above the threshold
n1.receiveSpike(20)

#If sendSpike is called, n1 will now fire a 5 mV spike, so I give this as an input to n2's receiveSpike:
n2.receiveSpike(n1.sendSpike())

#n2's membrane potential has changed to -75 because it received the spike:
print(n2.V_membrane)