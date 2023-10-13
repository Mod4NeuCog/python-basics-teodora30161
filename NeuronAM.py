#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 14:37:55 2023

@author: teostei
"""
class NeuronAM:
  def __init__(self, membrane_potential):
      self.membrane_potential = membrane_potential

import sys
membrane_potential = float(sys.argv[1])
if membrane_potential >= float(-65):
    print(5)
else:
    print(0)