#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 23:54:57 2023

@author: teostei
"""
#Exercise 3 lesson 3
#Input: float V_membrane
#Input: Array weight_array
#Input: Array current_array
#Input: Multiset synapse_bag
#synapse_potentials(V_membrane, weight_array, current_array, synapse_bag):
#   float V_new <- V_membrane
#   for i in (0, length(weight_array)):
#     V_new <- V_new +weight_array[i] * current_array[i]
#   new_bag <- synapse_bag + {V_new}
#   Return: new_bag
#Output: new_bag

import multiset
def synapse_potential(V_membrane, weight_array, current_array, synapse_bag):
    V_new = V_membrane
    for i in range(0, len(weight_array)):
        V_new += weight_array[i]* current_array[i]
        new_bag = synapse_bag + {V_new}
        return new_bag
    
print(synapse_potential(-75, [0.1,0.6], [1,4], multiset({-65}) + multiset({-65})))
    
#Exercise 4 lesson 3
#Adding a list to the previous algorithm 

def synapse_potential(V_membrane, weight_array, current_array, potential_list):
    V_new = V_membrane
    for i in range(0, len(weight_array)):
        V_new += weight_array[i]* current_array[i]
    new_list = potential_list
    potential_list.append(V_new)
    return new_list
def remove_potential(potential_list):
    popped_item = potential_list.pop(0)
    new_list = potential_list
    return [popped_item, new_list]

potentials = [-50, -80]
l = synapse_potential(-75, [0.1,0.5], [2,3], potentials)
print(l)
print(remove_potential)

#Exercise 5 lesson 3 FIFO
#Input: float V_membrane
#Input: Array weight_array
#Input: Array current_array
#Input: List[float] potential_list
#synapse_potentials(V_membrane, weight_array, current_array, potential_list):
#   float V_new <- V_membrane
#   for i in (0, length(weight_array)):
#     V_new <- V_new *weight_array[i] * current_array[i]
#   new_list <- potential_list.insert(0, V_new)
#   Return: new_list
#remove_potential(potential_list):
#   popped_item <- potential_list.pop(0)    
#   new_list = potential_list
#   return (popped_item, new_list)
#Output: potential_list

def synapse_potential(V_membrane, weight_array, current_array, potential_list):
    V_new = V_membrane
    for i in range(0, len(weight_array)):
        V_new += weight_array[i] * current_array[i]
    new_list = potential_list
    new_list.insert(0, V_new)
    return new_list
def remove_potential(potential_list):
    popped_item = potential_list.pop(0)
    new_list = potential_list
    return(popped_item, new_list)
