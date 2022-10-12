# VARIABEL

# a=10
# # print(a)


# y, z = 20, 5

# penjumlahan = y+z #nilai1 ditambah nilai2
# print("Hasil dari y+z =", penjumlahan)

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