import numpy as np

A = np.array([[-1, 2], [3, -2], [5, 7]])

# first we need found svd of A
U, d, VT = np.linalg.svd(A)
print('U is:')
print(U)
print('D is')
D = np.diag(d)
print(D)
print('VT is:')
print(VT)
print('------------------------------')

print('we can find D+ by one step. inverting it.cus d is diagonal marrix')
Dinv = np.linalg.inv(D)
print(Dinv)
print('So D plus is:')
D_plus = np.concatenate((Dinv, np.array([[0, 0]]).T), axis=1)
# axis=1 cus we want to calculate V*D+*UT not U*D*VT
print(D_plus)

A_plus = np.dot(VT.T, np.dot(D_plus, U.T))
print('Pseudoinverse of A is:')
print(A_plus)

print('------------------------------')

print('But good news. numpy has an func to calculating pinverse and do what we had done:')
print(np.linalg.pinv(A))

