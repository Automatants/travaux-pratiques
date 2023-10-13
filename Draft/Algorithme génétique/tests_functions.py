# -*- coding: utf-8 -*-
"""
@author: Thomas GAUTHEY

Test function for optimization
"""
import numpy as np
import matplotlib.pyplot as plt

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

def lvl7(X,show =False,legend='unavailable'):
    # Dimension minimum 10 et toujours PAIRE
    dist = 0
    nb_point = len(X)/2
    for i in range(0,len(X),2):
        dist += abs(np.cos(np.pi*i/nb_point) - X[i])
        dist += abs(np.sin(np.pi*i/nb_point) - X[i+1])
    if show:
        plt.ion()
        plt.figure('Dessin')
        plt.clf()
        for i in range(0,len(X),2):
            plt.scatter(X[i],X[i+1],color='r')
        theta = np.linspace(0,2*np.pi,100)
        plt.plot(np.cos(theta),np.sin(theta),color='white',label='dist :'+legend)
        plt.legend()
        plt.axis('equal')
        plt.show()
        plt.pause(0.1)
    return dist

def lvl8(X,show =False,legend='unavailable'):
    # Dimension minimum 20 et toujours PAIRE
    dist = 0
    nb_point = len(X)/2
    for i in range(0,len(X),2):
        dist += abs(np.cos(np.pi*i/nb_point)*(1+np.cos(np.pi*i/nb_point)) - X[i])
        dist += abs(np.sin(np.pi*i/nb_point)*(1+np.cos(np.pi*i/nb_point)) - X[i+1])
    if show:
        plt.ion()
        plt.figure('Dessin')
        plt.clf()
        for i in range(0,len(X),2):
            plt.scatter(X[i],X[i+1],color='r')
        theta = np.linspace(0,2*np.pi,100)
        plt.plot(np.cos(theta)*(1+np.cos(theta)),np.sin(theta)*(1+np.cos(theta)),color='white',label='dist :'+legend)
        plt.legend()
        plt.show()
        plt.pause(0.1)
    return dist

def lvl9(X,show =False,legend='unavailable'):
    # Dimension minimum 40 et toujours PAIRE
    dist = 0
    nb_point = len(X)/2
    for i in range(0,len(X),2):
        s = np.pi*i/nb_point
        dist += abs(16*np.sin(s)**3 - X[i])
        dist += abs(13*np.cos(s)-6*np.cos(2*s)-2*np.cos(3*s)-np.cos(4*s) - X[i+1])
    if show:
        plt.ion()
        plt.figure('Dessin')
        plt.clf()
        for i in range(0,len(X),2):
            plt.scatter(X[i],X[i+1],color='r')
        theta = np.linspace(0,2*np.pi,100)
        plt.plot(16*np.sin(theta)**3,13*np.cos(theta)-6*np.cos(2*theta)-2*np.cos(3*theta)-np.cos(4*theta),color='white',label='dist :'+legend)
        plt.legend()
        plt.show()
        plt.pause(0.1)
    return dist

def lvl10(X,show =False,legend='unavailable'):
    # Dimension minimum 80 et toujours PAIRE
    f1 = lambda x : (abs(x)/x)*(abs(x)- .5*abs(abs(x)-2) - .25*abs(abs(x)-2) - .25*abs(abs(x)-4) + (23/8)*(abs(abs(x)-8)-abs(abs(x)-12)) - (29/10)*(abs(abs(x)-16)-abs(abs(x)-21)) + .25*((abs(abs(x)-12)-abs(abs(x)-16)-2)**2) - 10*np.cos((np.pi/16)*(abs(abs(x)-4)-abs(abs(x)-8)+12)) -10 )
    f2 = lambda y : -((abs(y) - abs(abs(y)-1) + 1)/2)**2 + .25*(6*abs(abs(y)-1) - 11*abs(abs(y)-2) + 5*abs(abs(y)-4)) - 2*(abs(abs(y)-12)-abs(abs(y)-16)) - (12/1e5)*(abs(abs(y)-16) - abs(abs(y)-21) + 5)**5 - 6*np.sin((np.pi/16)*(abs(abs(y)-4) - abs(abs(y)-8) + 12)) +10
    dist = 0
    for i in range(0,len(X),2):
        s = -21 + 42*i/len(X) + 1e-4
        dist += abs(((f1(s) - X[i])**2) * (2*np.sin(f1(s) - X[i])))
        dist += abs(((f2(s) - X[i+1])**2) * (2+np.sin(f2(s) - X[i+1])))
    if show:
        plt.ion()
        plt.figure('Dessin')
        plt.clf()
        for i in range(0,len(X),2):
            plt.scatter(X[i],X[i+1],color='r')
        theta = np.linspace(-21,21,100)
        plt.plot(f1(theta),f2(theta),color='white',label='dist :'+legend)
        plt.legend()
        plt.show()
        plt.pause(0.1)
    return dist

def function_multi(X,show=False):
    #Dimension PAIRE dim >= 6
    #Restreindre à [-1.5,1.5] TOUTES LES VARIABLES
    x = [X[i] for i in range(0,len(X),2)]
    y = [X[i+1] for i in range(0,len(X),2)]
    dist1 = 0
    for i in range(len(x)):
        dist1 += (np.sqrt((x[i]**2 + y[i]**2))**2-1)**4
    dist2 = 0
    for i in range(len(x)):
        for j in range(len(x)):
            dist2 += np.sqrt((x[i]-x[j])**2 + (y[i]-y[j])**2)
    if show:
        plt.ion()
        plt.scatter(x,y,color='r')
        plt.show()
        plt.pause(0.1)  
    return [dist1,-dist2]

#Exemple de plot3D
#import matplotlib.pyplot as plt
#from matplotlib import cm
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#X,Y = np.meshgrid(np.linspace(-1,10,1000),np.linspace(-1,10,1000))
#Z = np.array(function_lvl_6([X,Y]))
#ax.plot_surface(X,Y,Z,cmap=cm.gist_ncar)
#plt.show()
