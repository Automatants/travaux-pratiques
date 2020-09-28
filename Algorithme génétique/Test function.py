# -*- coding: utf-8 -*-
"""
@author: Thomas GAUTHEY

Test function for optimization
"""
import numpy as np

def function_lvl_1(X):
    return (X-2)**2

def function_lvl_2(X):
    return 1 + (X+8)**2 - np.cos(4*np.pi*(X+8))

def function_lvl_3(X):
    '''Attention à restreindre la zone de recherche à [-500,500]'''
    return -X*np.sin(np.sqrt(abs(X)))

def function_lvl_4(X): #Entre -5.12 et 5.12
    return 20 + (X[0]**2 - 10*np.cos(2*np.pi*X[0])) + (X[1]**2 - 10*np.cos(2*np.pi*X[1]))
 
def function_lvl_5(X): #Entre -5.12 et 5.12
    return  1 - (1 + np.cos(12*np.sqrt(X[0]**2 + X[1]**2)))/(0.5*(X[0]**2 + X[1]**2)+2)

def function_lvl_6(X): #Entre -1 et 10
    a = [3,5,2,1,7]
    b = [5,2,1,4,9]
    c = [1,2,5,2,3]
    result = 0
    for i in range(len(a)):
        result += c[i]*np.exp(-(X[0]-a[i])**2/np.pi - (X[1]-b[i])**2/np.pi)*np.cos(np.pi*(X[0]-a[i])**2+np.pi*(X[1]-b[i])**2)
    return -result

#Exemple de plot3D
#import matplotlib.pyplot as plt
#from matplotlib import cm
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#X,Y = np.meshgrid(np.linspace(-1,10,1000),np.linspace(-1,10,1000))
#Z = np.array(function_lvl_6([X,Y]))
#ax.plot_surface(X,Y,Z,cmap=cm.gist_ncar)
#plt.show()