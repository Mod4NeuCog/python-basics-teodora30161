#Copying the classes from the previous exercise
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
    def __str__(self):
        return f"{self.type} type neuron (V={self.V_membrane})"

#I changed the constructors to automatically set the type

class PyramidalNeuron(NeuronalCell):
    def __init__(self, V_membrane):
        self.V_membrane = V_membrane
        self.type = "Pyramidal"
    def __str__(self):
        return super().__str__()

class OvoidNeuron(NeuronalCell):
    def __init__(self, V_membrane):
        self.V_membrane = V_membrane
        self.type = "Ovoid"
    def __str__(self):
        return super().__str__()
    
# Exercise 3: "Implement NeuronalNetwork composition example running a loop to execute neuron potential computation transitions"

class NeuronalNetwork():
    def __init__(self, neuron_list):
        self.neuron_list = neuron_list
        self.l = len(neuron_list)
    def __str__(self):
        newstring = "Neurons: "
        for x in self.neuron_list:
            newstring += str(x) + ", "
        return newstring
    #I'm making a serial connection between all neurons of the list
    def V_update(self, kickstart):
        self.neuron_list[0].receiveSpike(kickstart)
        for i in range(1,self.l):
            self.neuron_list[i].receiveSpike(self.neuron_list[i-1].sendSpike())
            
#I instantiate 3 neurons
neuron1 = NeuronalCell(-75, "blah")
neuron2 = PyramidalNeuron(-65)
neuron3 = OvoidNeuron(-65)

#I create a network with the 3 neurons
network1 = NeuronalNetwork([neuron1, neuron2, neuron3])

#The neurons in the network currently have membrane potentials of -75, -65, -65
print(network1)

#If I kickstart the potential in the first neuron with 10 mv or less, no spikes will be transmitted to the others
network1.V_update(10)
print(network1)

#I give the first neuron another 5 mv:
network1.V_update(5)

#Now the spike travels through the other neurons:
print(network1)