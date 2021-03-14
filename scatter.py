import numpy as np
import matplotlib.pyplot as plt
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2 # 0 to 15 point radii
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()
import matplotlib.pyplot as plt
from numpy.random import rand
fig, ax = plt.subplots()
for color in ['red', 'green', 'blue']:
                               n = 750
x, y = rand(2, n)
scale = 200.0 * rand(n)
ax.scatter(x, y, c=color, s=scale, label=color,
alpha=0.3, edgecolors='none')
ax.legend()
ax.grid(True) 