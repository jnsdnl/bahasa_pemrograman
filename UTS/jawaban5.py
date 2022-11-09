def jualan():
    a = "capucino"
    b = "teh"
    print ("Pilihan")
    print ("1.", a)
    print ("2.", b)
    print ("3. Exit")

def capucino():
    cap = "memilih capucino"
    print(cap)
    capucino = int(input("masukkan harga : "))
    ppn = 10/100
    total = capucino + (capucino*ppn)
    print("Jumlah yang harus di bayarkan : ", total)

def teh():
    teh = "memilih teh"
    print(teh)
    teh = int(input("masukkan harga : "))
    ppn = 10/100
    total = teh + (teh*ppn)
    print("Jumlah yang harus di bayarkan : ", total)

def Customer():
    nim = 20210801347
    nama = "Junius Daniel"
    print ("NIM : ", nim)
    print ("NAMA : ", nama)

while True:
    Customer()
    jualan()
    pil = int(input("masukkan pilihan : "))
    if pil == 1:
        capucino()
    elif pil == 2:
        teh()
    elif pil == 3:
        break
    else:
        print ("pilihan salah")