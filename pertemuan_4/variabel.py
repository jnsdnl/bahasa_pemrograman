#Variabel
print("====Variabel====")


def penjumlahan():

    a=int(input("masukkan angka pertama : "))
    b=int(input("masukkan angka kedua : "))
    c=a+b
    print("Total Penjumlahan", c)

while True:
    print("MENU")
    print("1. Penjumalahan")
    print("2.  Exit")
    choice = int(input("pilihanmu : "))
    if choice == 1:
        penjumlahan()
    elif choice == 2:
        break
    else:
        print("pilihan salah")


#Fungsional
print("====Fungsional====")

def input_alas_dan_tinggi ():
  alas = float(input('Masukkan alas: '))
  tinggi = float((input('Masukkan tinggi: ')))

  return alas, tinggi

def hitung_luas (alas, tinggi):
  return 0.5 * alas * tinggi

"""kalau fungsional, kita sendiri yang mengelola
hasil kembaliannya"""

# satu fungsi bisa dipanggil secara independen
#print(hitung_luas(5, 10))

# contoh dengan inputan alas dan tinggi
alas, tinggi = input_alas_dan_tinggi()
print(hitung_luas(alas, tinggi))


#Looping
print("====Looping====")

# looping python with range
for i in range(5):
    print(i)

#looping python with break
for i in range(1,11):
    print(i,' x ',i ,' = ',i*i)
    if i == 5:
        break

# looping python with continue
for i in range(1,11):
    if i == 5:
        continue
    print(i,' x ',i ,' = ',i*i)

# nested loop
listCity = ['Kalimantan', 'Sumatra', 'Sulawesi']
listPlace = ['West', 'North', 'South']
for city in listCity:
    for place in listPlace:
        print(city, place)



# contoh penambahan terkait break/continue
for val in "bahasa":
    if val == "h":
        continue
        #break
    print (val)
print ("selesai")

#OOP (Object Oriented Programing)
print("====OOP====")

class Segitiga:
  def __init__(self, alas, tinggi):
    self.alas = alas
    self.tinggi = tinggi

  def get_luas(self):
    return 0.5 * self.alas * self.tinggi

segitiga1 = Segitiga(5, 10)


print('luas segitiga1:', segitiga1.get_luas())


class Kotak:
    def input1(self):
        self.p = int(input("masukan panjang\t: "))
        self.l = int(input("masukan lebar\t: "))

    def luas(self):
        self.luas1 = self.p*self.l

kotak1 = Kotak()
kotak1.input1()
kotak1.luas()

print ("luas kotak\t:",kotak1.luas1)


#Prosedural
print("====Prosedural====")

def hitung_luas ():
  alas = float(input('Masukkan alas: '))
  tinggi = float(input('Masukkan tinggi: '))
  print('Luas =', 0.5 * alas * tinggi)

# kita bisa panggil berkali-kali
hitung_luas()
# panggil lagi
# hitung_luas()