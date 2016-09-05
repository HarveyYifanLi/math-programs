
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 14:56:58 2015

@author: yifanli
"""

import numpy as np
import matplotlib.pyplot as plt

nf = np.array([1.,2.,4.,5.]) ##number of copies or flavours of our new Baryo-lepto fermions.
print('nf is ',nf)
Mf=500. ### The mass of the new fermion is about 500 Gev.
Mz=91.1876 ### The mass of the Z boson,91.2 Gev
g_Mz=np.array([0.462798,0.647941,1.1719])##Defines gi at Mz which is 91.2 Gev, the mass of Z boson.
print('g at Mz is ',g_Mz)


#a_inverse=np.array([0.,0.,0.])
a_inverse=np.array([59.09292,29.64280,8.52514])
#a_inverse=np.array([58.0,31.0,11.0])

#a_inverse=np.array([25.0,31.0,10.0])
#for i in range(3):
#    a_inverse[i]=4*np.pi/(g_Mz[i]**2)## Gives ai^-1 at Mz based on gi at Mz
print('a-inverse is ',a_inverse)


C_Mz=2.*np.pi*(a_inverse[1]-a_inverse[2])+23./6*np.log(Mz)##which returns a scalar value


u=np.array([0.,0.,0.,0.])
Mu=np.array([0.,0.,0.,0.])
K1=np.array([0.,0.,0.,0.]) ##### Gives K1 

for i in range(4):
    u[i]=(C_Mz+nf[i]*2.*np.log(Mf))/(23./6+nf[i]*2.)## where u = log(Mu) in fact

    Mu[i]=np.exp(u[i])/1000. ##### Returns Mu from u : Mu=exp(u) 
    #K1[i]=float((2.*3.14159265358*a_inverse[0]-41./6*np.log(Mu[i]/Mz)-nf[i]*2./3*np.log(Mu[i]/Mf)))/(2.*3.14159265358*a_inverse[2]+7.*np.log(Mu[i]/Mz))

    K1[i]=(2.*np.pi*a_inverse[0]-41./6*np.log(Mu[i]/Mz)-nf[i]*2./3*np.log(Mu[i]/Mf))/(2.*np.pi*a_inverse[2]+7.*np.log(Mu[i]/Mz))
print('u is ',u)
print('Mu is ',Mu,'in Tev')
print('K1 is ',K1)
   
bBnew = np.array([0.,0.,0.,0.])  
bLnew = np.array([0.,0.,0.,0.])
bSMB = 8.0/3
bSML = 6.0

for i in range(4):
    bBnew[i]=float(3*(4*nf[i]+1))/nf[i]**2
print('bBnew is ',bBnew)
for i in range(4):
    bLnew[i]=bBnew[i]+10.0/3
print('bLnew is ',bLnew)

BB = np.array([0.,0.,0.,0.])
BL = np.array([0.,0.,0.,0.])

for i in  range(4):
    BB[i]=bSMB+bBnew[i]*np.log(Mu[i]/Mf)/np.log(Mu[i]/Mz)    
print('BB is ',BB)
for i in  range(4):
    BL[i]=bSML+bLnew[i]*np.log(Mu[i]/Mf)/np.log(Mu[i]/Mz)    
print('BL is ',BL)








    
    