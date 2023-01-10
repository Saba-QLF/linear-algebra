import numpy as np
import matplotlib.pyplot as plt

d = np.linspace(0, 50, 1000)

mark_1 = d
mark_2 = 4 * (d-30)

fig, ax = plt.subplots()
plt.title("making energy by machines")
plt.xlabel("time (in days)")
plt.ylabel("energy (in kj/day)")
ax.set_xlim([0, 50])
ax.set_ylim([0, 60])
ax.plot(d, mark_1, c='green')
ax.plot(d, mark_2, c='brown')
plt.axvline(x=40, color='purple', linestyle='--')
plt.axhline(y=40, color='purple', linestyle='--')
plt.show()
