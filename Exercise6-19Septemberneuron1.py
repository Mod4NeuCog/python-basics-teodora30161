def Simulate():  #Simulate method is calling the other two functions compute_membrane_potential and new_membrane_potential2
    spike_value = (float(input()))
    new_membrane_potential = 3
    compute_membrane_potential(new_membrane_potential)
    new_membrane_potential2(spike_value, new_membrane_potential)
    
    
def compute_membrane_potential(spike_value, current_membrane_potential=0.0):
    new_membrane_potential = current_membrane_potential + spike_value
    if new_membrane_potential >= -65:
        return 5, new_membrane_potential
    else:
        return 0, new_membrane_potential


def new_membrane_potential2(new_membrane_potential, spike_value):
    current_membrane_potential = 45
    new_membrane_potential = current_membrane_potential + spike_value
    print(new_membrane_potential)

def main():     #main is calling Simulate method
    Simulate()
if __name__ == "__main__":
    main()