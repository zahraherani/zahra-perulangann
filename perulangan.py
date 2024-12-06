'''
#list for in
listkota = [
    'Jakarta','Surabaya','Depok','Bekasi','Solo','Yogyakarta','Semarang','Makassar'
]
for kota in listkota:
    print(kota)
#for dengan fungsi range()
##0 sampai 4
for i in range(5):
    print("Perulangan ke:", i)
#mencari bil.ganjil dgn for
for bil_ganjil in range (1,12,2):
    print(bil_ganjil)
# dimulai angka 1 dan setelah angka 2 dan 12 batas angkanya
#for dengan tuple
tupleBuah = ('Mangga','Jeruk','Apel','Pir')
for buah in tupleBuah:
    print(buah)
# for else
listkota = [
    'Jakarta','Surabaya','Depok','Bekasi','Solo','Yogyakarta','Semarang','Makassar'
]
for kota in listkota:
    print(kota)
else:
    print('Semua kota telah ditampilkan')
#for else + break
listkota = [
    'Jakarta','Surabaya','Depok','Bekasi','Solo','Yogyakarta','Semarang','Makassar'
]

kotayangdicari = input('Ketik nama kota yang kamu cari: ')
for i, kota in enumerate (listkota):
    #kita ubah katanya ke  lowercase agar
    #menjadi case insensitive
    if kota.lower()== kotayangdicari.lower():
        print('Kota yang anda cari berada pada indeks', i)
        break
    else:
        print('Maaf, kota yang anda cari tidak ada')
#perulangan menggnakan while

while (1 + 2 == : 'halo dunia')
    print ('halo dunia')
'''

listkota = ['Jakarta','Surabaya','Depok','Bekasi','Solo','Yogyakarta','Semarang','Makassar']
#bermain index
i = 0
while i < len (listkota):
    print(listkota[i])
    i += 1

a = int(input('Masukan bilangan ganjil lebih dari 50: '))
while a % 2 != 1 or a <= 50:
    a = int(input('Salah, masukan lagi: '))

print('Benar')

listkota = ['Jakarta','Surabaya','Depok','Bekasi','Solo','Yogyakarta','Semarang','Makassar']

kotayangdicari = input('Masukan nama kota yang dicari: ')

i = 0
while i < len (listkota):
    if listkota[i].lower() == kotayangdicari.lower():
        print('Ketemu di index', i)
        break
    print('Bukan', listkota[i])
    i += 1
else:

  print('Maaf, kota yang anda cari tidak ditemukan.')