import numpy as np
import matplotlib.pyplot as plt

a = 1.
s = np.random.weibull(a, 10000)
plt.hist(s, bins=100)
plt.show
