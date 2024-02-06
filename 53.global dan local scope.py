
def fungsi():
    nama_local = 'ucup'     # variabel local scope
fungsi()
# print(nama_local) #tidak bisa dilakukan

# contoh : 1 penggunaan akses
def say_otong():
    print(f'hello {nama}')

nama = 'otong'
say_otong()

# contoh 2: merubah varibel global
angka = 0
name = 'ucup'
def ubah(nilai_baru,nama_baru):
    global angka # fungsi ini mendapat akses merubah angka
    angka = nilai_baru
    global name
    name = nama_baru

print(f'sebelum {angka,name}')
print(f'sebelum {name}')
ubah(10,'otong')

print(f'sesudah {angka,name}')
print(f'sesudah {name}')

angka = 0

for i in range(0,5):
    angka += i
    angka_dummy = 0
print(angka)
print(angka_dummy)


for i in range(0,5):
