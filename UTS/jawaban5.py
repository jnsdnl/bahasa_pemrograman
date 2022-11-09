def penjumlahan():

    a=int(input("NIM"))
    b=str(input("NAMA"))
    print (a)
    print (b)

    c=int(input("masukkan angka pertama : "))
    d=int(input("masukkan angka kedua : "))
    e=c+d
    print("Total Penjumlahan", e)

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