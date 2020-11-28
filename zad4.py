plik = open("cyfry.txt")
dane = plik.read().split()
zapis = open("zadanie4.txt", 'w+')
nieparzyste=0
for i in dane:
    if int(i)%2==1:
        nieparzyste+=1


print('4.1: '+ str(nieparzyste))
zapis.write('4.1: '+ str(nieparzyste) + '\n')



maks = 0
maks_l = 0
mini = 9999999999999999999
mini_l = 0
for j in dane:
    suma = 0
    for k in j:
        suma+=int(k)
    if suma>maks:
        maks=suma
        maks_l=j
    if suma < mini:
        mini=suma
        mini_l=j
print("zad 4.2: "+str(maks_l)+", "+str(mini_l))
zapis.write("zad 4.2: "+str(maks_l)+", "+str(mini_l) + '\n')
print("zad 4.3: ")
zapis.write("zad 4.3: \n")
for k in dane:
    asc = True
    for ii in range(1, len(k)):
        if int(k[ii]) <= int(k[ii-1]):
            asc = False
    if asc:
        print(k)
        zapis.write(k+'\n')

