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
 def generuj(liczba, ilosc):
     return np.logspace(1,ilosc,num=ilosc, base=liczba)
 print(generuj(2,4))

#ZAD5
def generuj(n):

    mat_diag = np.diag([a for a in range(n, 0, -1)])

    return mat_diag


print(generuj(5))

#ZAD6

malina = np.array(list('malina'))
mrowka = np.array(list('mrówka'))
armata = np.array(list('armata'))
armata = np.flip(armata)

 wykreslanka = np.zeros((6,6), dtype='str')

 print(wykreslanka)

 wykreslanka = np.diag(mrowka)
 wykreslanka[:, 0] = malina
 wykreslanka[5,::-1] = armata
 #wykreslanka[5,:] = armata
 print(wykreslanka)
 print("")
 wykreslanka[:, 0] = mrowka
 wykreslanka[5,::-1] = armata
 for a in range(5):
     wykreslanka[a,a] = malina[a]
 print(wykreslanka)


#ZAD7

def macierz(n):
    mat = np.arange(n*n)
    mat = mat.reshape(n,n)

    return mat

print(macierz(5))

#ZAD8
 def zad8(tab, kierunek='poziomo'):
     print(tab)
     if kierunek == 'poziomo':
         # nieparzysta liczba wierszy
         if tab.shape[0] % 2 != 0:
             print("Tablica posiada nieprzystą liczbę wierszy")
             return
         p1 = tab[0:int(tab.shape[0]/2), :]
         p2 = tab[int(tab.shape[0]/2):, :]
         print("***** część 1 *****")
         print(p1)
         print("***** część 2 *****")
         print(p2)
     elif kierunek == "pionowo":
         if tab.shape[1] % 2 != 0:
             print("Tablica posiada nieprzystą liczbę kolumn")
             return
         p1 = tab[:, 0:int(tab.shape[1]/2)]
         p2 = tab[:, int(tab.shape[1] / 2):]
         print("***** część 1 *****")
         print(p1)
         print("***** część 2 *****")
         print(p2)

 zad8(np.arange(36).reshape((6,6)), kierunek='pionowo')

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

