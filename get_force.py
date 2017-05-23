#edited by Jin Zhang
# This code help you to get the force from VASP calculation 
import numpy as np
import matplotlib.pyplot as plt
data =[]
m=[]
with open ("OUTCAR") as outcar:
    data_0 = outcar.readlines()  # read each line
    length = len(data_0)
    print (len(data_0))
    for i in range(length):
        if "TOTAL-FORCE" in data_0[i]:  # find the line which includes "TOTAL-FORCE"
            index0 = i; 
            index_beg = i+2
            print('yes')
        if "total drift" in data_0[i]: # find the line which includes "total drift"
            index1 = i
            index_over =  index1-1
            print(index_over)
    
    for i in range(index_beg, index_over):   # read from line-index_beg to line-index_over
        j = data_0[i]
        j = j.split()
        m.extend(j)
m = np.asarray (m, dtype = np.float64) # convert to array
n = int(m.size)
n = int(n/6)
m = m.reshape(n,6)
force = m[:,3:]
np.savetxt("force", force)


      

