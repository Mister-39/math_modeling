import numpy as np
def ctan(alpha=1):
    x=1/np.tan(alpha)
    return x
print(ctan(np.pi))