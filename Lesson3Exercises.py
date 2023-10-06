#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 14:54:23 2023

@author: teostei
"""
import time
V_threshold = -65
V_membrane = -75
V_rest = -75
t_start = time.time()


def delta(input, V_mem):
    V_mem = V_mem + input
    return(V_mem)

def lambda_dtss(V_mem):
    
    if(V_mem >= V_threshold):
        global V_membrane
        V_membrane = V_rest
        return(5)
    else:
        return(0)

## Define a function to simulate neuron behaviour
def simulate(inputSpikeList,t_end,c):
    t=0 #real time
    n=0 # simulation time
    global V_membrane
    while(t < t_end):
        t_current = time.time() - t_start
        output_neuron = lambda_dtss(V_membrane)
        
        V_membrane = delta(inputSpikeList[n],V_membrane)
        print("current time=",t_current)
        #print("V_membrane=",V_membrane)
        print("t=",t,V_membrane,output_neuron)
        
        n=n+1
        t=n*c
        #print("n=",n,"t=",t)
    return(V_membrane) 

def updated_membrane_potential(inputSynapticRates, inputSynapticWeigh):  
    new_membrane_potential = 0 
    for i in range(0,len(inputSynapticRates)):               
       new_membrane_potential = new_membrane_potential + inputSynapticRates[i] * inputSynapticWeigh[i]
    print("the new membrane potential based on synaptic rate and weight", new_membrane_potential)

def main():
    inputSpikeList = [0,5,5,0,0,0,0,5]
    inputSynapticWeigh = [10, 10, 20, 10, 20, 10, 20, 10]
    inputSynapticRates = [5, 5, 5, 5, 5, 5, 5, 5]
    updated_membrane_potential(inputSynapticRates, inputSynapticWeigh)
    t_end = 3.5
    c = 0.5
    simulate(inputSpikeList,t_end,c)
    
# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()