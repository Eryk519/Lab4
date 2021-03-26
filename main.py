import numpy as np
#ZAD1
a = np.arange(3,48,3,)
print(a)
#ZAD2
a = np.arange(1,20,1.5)
print(a)
b = a.astype('int64')
print(b)
#ZAD3
def numpyList(n):
    tab = np.arange(1, n*n+1, 1)

    return tab

print(numpyList(10))

#ZAD4


#ZAD5
def generuj(n):

    mat_diag = np.diag([a for a in range(n, 0, -1)])

    return mat_diag


print(generuj(5))

#ZAD6

#ZAD7

def macierz(n):
    mat = np.arange(n*n)
    mat = mat.reshape(n,n)

    return mat

print(macierz(5))

#ZAD8


#ZAD9
a = 0
b = 1
list = []

for i in range(25):
    list.append(a)
    b += a
    a = b-a

numpyList = np.array(list)
numpyList = numpyList.reshape(5,5)

print(numpyList)

