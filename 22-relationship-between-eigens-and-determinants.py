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


X = np.array([[1, 2, 4],
              [2, -1, 3],
              [0, 5, 1]])
det = np.linalg.det(X)

print(det)

lambdas, V = np.linalg.eig(X)
print(lambdas)

print(np.product(lambdas))
# its multiplying all elements of the array
# as you can see, its equal to determinan of our matrix
print('--------------------------------------')

B = np.array([[1, 0], [0, 1]])
plot_vectors([B[0], B[1]],
             ['lightblue', 'lightgreen'])
plt.xlim(-1, 3)
plt.ylim(-1, 3)
plt.show()

N = np.array([[-4, 1], [-8, 2]])
print(np.linalg.det(N))
NB = np.dot(N, B)
print(NB)
plot_vectors([B[0], B[1], NB[0], NB[1]],
             ['lightblue', 'lightgreen', 'blue', 'green'])
plt.xlim(-9, 6)
plt.ylim(-9, 3)
plt.show()


