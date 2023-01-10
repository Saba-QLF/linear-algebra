import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 40, 1000)
# print(t)
# produced 1000 numbers in range (0, 40) with equal steps

d_r = 2.5 * t
d_s = 3 * (t-5)
# our two equation

fig, ax = plt.subplots()
# subplots(row, column, which-place)
plt.title("A Bank Robber Caught")
plt.xlabel("time (in minutes)")
plt.ylabel("distance (in km)")
ax.set_xlim([0, 40])
ax.set_ylim([0, 100])
ax.plot(t, d_r, c='green')
ax.plot(t, d_s, c='brown')
plt.axvline(x=30, color='purple', linestyle='--')
plt.axhline(y=75, color='purple', linestyle='--')
# we can find the solutions of the problem, then draw purple lines
plt.show()

