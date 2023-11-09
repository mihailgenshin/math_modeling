import numpy as np
h = 100 
alf = np.pi/3
b = 30
g = 10
p = 3.14
a = p/3
b = p/6 
V =np.sqrt((g*h*np.tan(b)**2) / (2 * np.cos(a)**2 *(1 - np.tan(b) * np.tan(a))))
print(V)