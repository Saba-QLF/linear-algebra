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


A = np.array([[-1, 4], [2, -2]])
lambdas, V = np.linalg.eig(A)
# Eigen Vectors
print(V)
# Eigen Values
print(lambdas)

print('------------------------------------')
eig_vec_1 = V[:, 0]
eig_val_1 = lambdas[0]
print(eig_vec_1, eig_val_1)

print('------------------------------------')
Av1 = np.dot(A, eig_vec_1)
print(Av1)
print(eig_val_1 * eig_vec_1)
# they are equal: Av = lambda * v
print('------------------------------------')

# this rules works for others eigenvectors too
eig_vec_2 = V[:, 1]
eig_val_2 = lambdas[1]
Av2 = np.dot(A, eig_vec_2)

plot_vectors([Av1, eig_vec_1, Av2, eig_vec_2],
             ['blue', 'lightblue', 'green', 'lightgreen'])
plt.xlim(-1, 4)
plt.ylim(-3, 2)
plt.show()