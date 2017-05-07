#Edited by Jin Zhang 04/05/2016
# This script convert direct lattic vector to reciprocal lattice vector

import numpy as np
import matplotlib.pyplot as plt
from math import pi

#direct lattice vector
a1 = [float(x) for x in input('Enter a1:  ').split()]
a2 = [float(x) for x in input('Enter a2:  ').split()]
a3 = [float(x) for x in input('Enter a3:  ').split()]
type_recip = input('Enter the type (R --- reciprocal (with 2pi); V --- vasp (without 2pi) :  ') # R --- reciprocal (with 2pi); V --- vasp (without 2pi).

#volume (unit: angstrom^3)
V= np.dot (np.cross (a1, a2), a3)  

#reciprocal lattice vector (unit: angstrom^2)
b1_a2_a3 = np.cross (a2, a3)
b2_a3_a1 = np.cross (a3, a1)
b3_a1_a2 = np.cross (a1, a2)

#consider 2pi
if type_recip == "R":
    b1 = [((2*pi)/V)*i for i in b1_a2_a3] # unit: angstrom^(-1)
    b2 = [((2*pi)/V)*i for i in b2_a3_a1]
    b3 = [((2*pi)/V)*i for i in b3_a1_a2]
    b1 = [float(round (i, 9)) for i in b1]
    b2 = [float(round (i, 9)) for i in b2]
    b3 = [float(round (i, 9)) for i in b3]
    b = [b1, b2, b3]
    print (b)
    np.savetxt("RecipLatt_with_2pi.txt", b)
    
#without considering 2pi, like VASP 
if type_recip == "V":
    b1 = [(1/V)*i for i in b1_a2_a3]  # unit: angstrom^(-1)
    b2 = [(1/V)*i for i in b2_a3_a1]
    b3 = [(1/V)*i for i in b3_a1_a2]
    b1 = [float(round (i, 9)) for i in b1]
    b2 = [float(round (i, 9)) for i in b2]
    b3 = [float(round (i, 9)) for i in b3]
    b = [b1, b2, b3]
    print (b)
    np.savetxt("RecipLatt_without_2pi.txt", b)


