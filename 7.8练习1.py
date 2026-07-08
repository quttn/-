import numpy as np
a = np.random.randint(0,10,(3,4))
print(a)
b = a.reshape(4,3)
print(b)
c = a.T
print(c)
d = c[c>5]
print(d)

