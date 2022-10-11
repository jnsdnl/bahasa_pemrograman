#Contoh Operator Aritmatika
a="operator aritmatika"
d="operator aritmatika digunakan memecahkan kasus yang berhubungan dengan hitunh menghitung"

print(a)
print(d)

y, z = 20, 5

penjumlahan = y+z #nilai1 ditambah nilai2
print("Hasil dari y+z =", penjumlahan)

#Contoh Operator perbandingan
b= "operator perbandingan"
a="operator perbandingan bertugas untuk membandingkan antar dua operan"

print(b)
print(a)

y, z = 20, 5

print("apakah y lebih besar dari z")
print("y > z \t:", y>z) #Lebih besar

#Contoh Operator Penugasan
c= "Operator Penugasan"
b="operator penugasan untuk memasukkan suatu nilai ke dalam variabel"

print(c)
print(b)

j = 5
j += 3

print("hasil dari penambahan dari input 1 ditambah dengan input 2 dengan variabel yang sama")
print (j)

#Contoh Operator Logika/Boolean
d= "Operator Logika/Boolean"
c="Operator Logika digunakan untuk membandingkan dua Operand atau dua nilai yang bertipe Boolean dan akan menghasilkan nilai Boolean yaitu TRUE atau FALSE"

print(d)
print(c)

y = True
z = False
l = y and z

print("hasil dari logika AND")
print ("True or False =", l)

#Contoh Operator Keanggotaan
q= "Operator Keanggotaan"
w= "Fungsi dari operator ini adalah untuk memeriksa apakah suatu nilai merupakan salah satu anggota dari variabel berjenis sequence atau tidak"

print(q)
print(w)

x = (2,5,8)
y = 8

print ("hasil dari operator in")
print (8 in x)

#Contoh Operator Identitas
g= "Operator identitas"
o= "Tugasnya adalah untuk mengetahui apakah dua buah variabel merupakan objek yang sama atau memiliki nilai yang sama atau tidak"

print(g)
print(o)

h = 8
k = h

print ("hasil dari operator is")
print (k is h)

#Contoh Operator Bitwise
l="Operator Bitwise"
m="Jenis operator terakhir ini hampir sama seperti Operator Logika, akan tetapi operator ini melakukan operasi berdasarkan bilangan bit/biner"

print(l)
print(m)

print("biner dari angka 0")
print(format(0, '08b'))

v= 1
p= 22

print("[and]")
print('v & p =', v & p)
print(format(v, '08b'), '&', format(p, '08b'), '=', format(v & p, '08b'), '\n')