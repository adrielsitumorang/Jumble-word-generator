import numpy as np
import random

nama_depan = input('masukkan nama depan: ') 
nama_belakang = input('masukkan nama belakang: ')

jumlah_nama_depan = 0
for element in nama_depan: 
    jumlah_nama_depan += 1

jumlah_nama_belakang = 0
for element in nama_belakang: 
    jumlah_nama_belakang += 1 

d = np.zeros((27,80))

posisi_namdep_i= random.randint( 0,26)
posisi_namdep_j= random.randint( 0,79)
posisi_nambel_i= random.randint( 0,26)
posisi_nambel_j= random.randint( 0,79)

while (posisi_namdep_i == posisi_nambel_i):
    posisi_nambel_i = random.randint( 0,26)

k=0
l=0

if (posisi_namdep_j + jumlah_nama_depan <= 79):
    k = posisi_namdep_j
    for element in nama_depan:
        d[posisi_namdep_i][k] = float(ord(element))
        k+=1
else:
    if (posisi_namdep_i + jumlah_nama_depan <= 26):
        l = posisi_namdep_i 
        for element in nama_depan:
            d[l][posisi_namdep_j] = float(ord(element))
            l+=1 
    else:
        l = posisi_namdep_i 
        for element in nama_depan:
            d[l][posisi_namdep_j] = float(ord(element))
            l-=1

if (posisi_nambel_j + jumlah_nama_belakang <= 79):
    m = posisi_nambel_j
    for element in nama_belakang:
        d[posisi_nambel_i][m] = float(ord(element))
        m+=1
else:
    if (posisi_nambel_i + jumlah_nama_belakang <= 26):
        n = posisi_nambel_i 
        for element in nama_belakang:
            d[n][posisi_nambel_j] = float(ord(element))
            n+=1 
    else:
        n = posisi_nambel_i 
        for element in nama_belakang:
            d[n][posisi_nambel_j] = float(ord(element))
            n-=1


i=0
j=0

for i in range (27):
    for j in range (80):
        if (not d[i][j]):
            d [i][j] = random.randrange(97, 97 + 26)

for i in range (27):
    for j in range (80):
        if(j != 79):
            print(chr(int(d[i][j])).upper(), end = ' ')
        else:
            print(chr(int(d[i][j])).upper())