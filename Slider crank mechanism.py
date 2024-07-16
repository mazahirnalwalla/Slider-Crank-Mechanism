import numpy as np
import matplotlib.pyplot as plt
import scipy.misc as sci
from numpy import sin, cos, pi
from scipy.misc import derivative

r = float(input("Enter length of the crank in mm= "))
c = float(input("Enter the length of the connecting rod in mm= "))
rpm = float(input("enter the rotational speed in rpm= "))

omega = (2*pi*rpm)/60 #rotational speed in rad/sec

def disp(t): #displacement function with respect to time
    d1 = r*cos(omega*t)
    d2 = ((c**2)-(r**2*(sin(omega*t))**2))**(1/2)
    return d1+d2

def vel(t): #velocity function with respect to time
    return derivative(disp,t)

def acc(t):
    return derivative(vel,t)

t0 = float(input("How much time is the mechanism moving for in sec? "))
time = np.linspace(0,t0,1000)

x = disp(time)
v = vel(time)
a = acc(time)

theta = omega*time
theta1 = theta*180/pi

plt.figure(figsize=(5,15))

plt.subplot(3,1,1)
plt.plot(theta,x,color="yellow")
plt.title("Graphs of a slider crank mechanism")
plt.ylabel("Displacement in mm")
plt.grid(color="blue")

plt.subplot(3,1,2)
plt.plot(theta,v,color="orange")
plt.ylabel("Velocity in mm/s")
plt.grid(color="blue")

plt.subplot(3,1,3)
plt.plot(theta,x,color="red")
plt.xlabel("Angles rotated in radian")
plt.ylabel("Accelaration in mm/s**2")
plt.grid(color="blue")

plt.show()