# -*- coding: utf-8 -*-
"""
Created on Tue May 26 17:39:32 2015

@author: yifanli
"""

import numpy as np
import matplotlib.pyplot as plt
### Solve a linear system
### useful links for linear algebra 
A=np.matrix([[-13,2,4],[2,-11,6],[4,6,-15]])### Do not forget the very outer square bracket in the declaring matrix
B=np.array([5,-10,5])
C=np.linalg.solve(A,B)
D=np.linalg.eig(A)###Compute the eigenvalues and right eigenvectors of a square array.
e=np.linalg.eigvals(A)###Compute the eigenvalues of a general matrix.
print C ,'\n'
print D ,'\n'
print e ,'\n'

### plot problems 
x=np.linspace(-10.0,10.0,500)
y=x**4*np.exp(-2*x)
plt.plot(x,y,'r-')
plt.plot(x,(x**2*np.exp(-x)*np.sin(x**2))**2,'b-')

plt.xlabel('x')
plt.ylabel('y')
plt.xlim(-11,-5)
#plt.ylim(0,1)
plt.legend(['first graph','second graph'],loc='upper right')


"""
now we are trying to define a function and run a program
to find the first several prime numbers using this program.
"""
### firstly define a function IsPrime() that will be called later.
def IsOdd(number):
    if number%2!=0:
        return True;
    else :
        return False;
    return;
    
count=0;
number=1;
Oddsneeded=100;

while count<Oddsneeded:
    if IsOdd(number):
        print number;
        count+=1;
    number +=1;

### print number exercise
a=123456.7722839;
print "this will be %+.6f" % a





















