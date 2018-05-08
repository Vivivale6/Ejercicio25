import numpy as np 
import matplotlib.pyplot as plt 

radius = 64694606000
velocity = 41970
G = 6.674*10**(-11)
M = 1.989*10**(30)

def beta(alpha,r,v):
	return (v**2)/r**(1-alpha)

al = np.linspace(0, 5.0, 500)
be = beta(al,radius, velocity)
be_2 = G*M
sigma_beta = np.var(be)

def normalizacion(b1, b2, sig):
	return np.exp(-((b2-b1)**2.0)/(2.0*sig))

norma_alpha = normalizacion(be,be_2,sigma_beta)

def probabilidad(datos, n):
	return n*(np.ones(datos))/datos

prob = probabilidad(500,norma_alpha)

plt.plot(be,prob)
plt.savefig("grafica25.png")
