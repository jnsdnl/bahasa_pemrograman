#perulangan menggunakan for

for baris in range(5):
  for kolom in range(7):
    print('o', end='')
  else:
    print('')

print("|---------------------|")
#perulangan menggunakan while

listKota = [
  'Jakarta', 'Bogor', 'Depok', 'Tanggerang', 'Bekasi'
]

print("JABODETABEK")

i = 0
while i < len(listKota):
  print(listKota[i])
  i += 1
  print('---------')

#perulangan menggunakan while - else
print("|---------------------|")

listNama = [
  'Junius', 'Omar', 'Jery', 'Fikri', 'Evan',
  'Angga', 'Hibrizi', 'Nurudin'
]

NamaYangDicari = input('Masukkan nama yang dicari: ')

i = 0
while i < len(listNama):
  if listNama[i].lower() == NamaYangDicari.lower():
    print('Ketemu di index', i)
    break

  print('Bukan ', listNama[i])
  i += 1
else:
  print('Maaf, nama yang anda cari tidak ditemukan.')