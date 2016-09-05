# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 19:07:18 2016

@author: yifanli
"""

import numpy as np
import matplotlib.pyplot as plt

u0=-50
xe=7
a0=0.6
m=0.5
k=5 #radial quantum number  appeared in the energy eigenvalues
n=0 #Principal quantum number
E=np.zeros(k)
x = np.arange(0, 30, 0.001)

y=u0/(1+np.exp((x-xe)/a0))-u0*np.exp((x-xe)/a0)*(a0*(1+np.exp((x-xe)/a0))**2)**(-1);
#y=u0/(1+np.exp((x-xe)/a0));
##Define all the parameters for the superpotential and then the Reference potential Vtilde
l=n-2*k #angular quantum number
c=l*(l+1)/(2*m*a0**2)
U=2*m*(c+u0)
alfa=1/a0
s2=-alfa/2+np.sqrt((alfa/2)**2+2*m*c)
s1=U/(2*s2)-s2/2
##Define the Superpotential related quantities
W=-1/np.sqrt(2*m)*(s1+s2*np.exp(-alfa*(x-xe))/(1+np.exp(-alfa*(x-xe))))
W1=-1/np.sqrt(2*m)*s2*(-alfa)*np.exp(-alfa*(x-xe))/(1+np.exp(-alfa*(x-xe)))**2 # W prime 
#Wsq=1/2*m*(s1**2+s2**2*np.exp(-2*alfa*(x-xe))/(1+np.exp(-alfa*(x-xe)))**2+2*s1*s2*np.exp(-alfa*(x-xe))/(1+np.exp(-alfa*(x-xe))))
Wsq=W**2
Vtilde=-(0.25*Wsq-0.5*W1) # the Reference potential
#plt.plot(x,Vtilde)

for i in range(k):
    #if i==0:
    #  E[i]=u0/2
    #   print(i,E[i])
    #else :
    #  E[i]=u0/2-(1*(8*m*a0**2)**(-1)*i**2+(-u0)/(2*i))
     #  print(i,E[i])
    #E[i]=(-1)/(2*m*a0**2)*(1/16*(2+2*i)**2+4*(m*(-u0)*a0**2/1)**2/(2+2*i)**2+m*(-u0)*a0**2/1)
    E[i]=(-1)/(2*m*a0**2)*(1/16*(2+2*(i+2))**2+4*(m*(-u0)*a0**2/1)**2/(2+2*(i+2))**2+m*(-u0)*a0**2/1)
    print i,E[i]
    l=n-2*(i+1) #Radial quantum number
    c=l*(l+1)/(2*m*a0**2)
    U=2*m*(c+u0)
    alfa=1/a0
    s2=-alfa/2+np.sqrt((alfa/2)**2+2*m*c)
    s1=U/(2*s2)-s2/2
    ##Define the Superpotential related quantities
    W=-1/np.sqrt(2*m)*(s1+s2*np.exp(-alfa*(x-xe))/(1+np.exp(-alfa*(x-xe))))
    W1=-1/np.sqrt(2*m)*s2*(-alfa)*np.exp(-alfa*(x-xe))/(1+np.exp(-alfa*(x-xe)))**2 # W prime 
    #Wsq=1/2*m*(s1**2+s2**2*np.exp(-2*alfa*(x-xe))/(1+np.exp(-alfa*(x-xe)))**2+2*s1*s2*np.exp(-alfa*(x-xe))/(1+np.exp(-alfa*(x-xe))))
    Wsq=W**2
    Vtilde=-(0.25*Wsq-0.5*W1) # the Reference potential
    plt.plot(x,Vtilde,label=i+1)
    plt.ylabel('Vtilde(x) for radial quantum number k=1,2,3,4,5 and n=0 ')
    plt.legend(bbox_to_anchor=(1.05, 1), loc=1, borderaxespad=0.)
    

plt.figure()
plt.xlim(-5,40)
plt.ylim(-60,40)
plt.xlabel('x')
plt.ylabel('V(x) and Vtilde(x) when n=0 k=5')
plt.plot(x,y,color='r',label='V(x)')
#plt.plot(x,Wsq)
#plt.plot(x,W1)
plt.plot(x,Vtilde,label='Vtilde(x),k=5')
plt.legend(bbox_to_anchor=(1.05, 1), loc=1, borderaxespad=0.)


