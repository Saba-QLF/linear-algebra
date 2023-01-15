import numpy as np
import matplotlib.pyplot as plt

def plot_vectors(vectors, colors):
    plt.figure()
    plt.axvline(x=0, color='lightgray')
    plt.axhline(y=0, color='lightgray')

    for i in range(len(vectors)):
        x = np.concatenate([[0, 0], vectors[i]])
        plt.quiver([x[0]], [x[1]], [x[2]], [x[3]],
                   angles='xy', scale_units='xy',
                   scale=1, color=colors[i])


v = np.array([3, 1])
E = np.array([[1, 0], [0, -1]])
Ev = np.dot(E, v)
plot_vectors([v, Ev], ['lightblue', 'blue'])
plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.show()

F = np.array([[-1, 0], [0, 1]])
Fv = np.dot(F, v)
plot_vectors([v, Fv], ['lightblue', 'blue'])
plt.xlim(-4, 4)
plt.ylim(-1, 5)
plt.show()

A = np.array([[-1, 4], [2, -2]])
Av = np.dot(A, v)
plot_vectors([v, Av], ['lightblue', 'blue'])
plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.show()

# concatenate vectors
# np.matrix(v).T
# this code make it 2D vector
v2 = np.array([-3, -1])
v3 = np.array([-1, 1])

V = np.concatenate((np.matrix(v).T,
                    np.matrix(v2).T,
                    np.matrix(v3).T),
                   axis=1)
print(V)


