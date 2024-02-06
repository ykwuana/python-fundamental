
# contoh 1
def say_hello(nama = 'ganteng'):
    print(f'hallo {nama}')

say_hello()

# contoh 2
def sapa_dia(nama,pesan = 'apa kabar'):
    print(f'hai {nama},{pesan}')

sapa_dia('dudung')

# contoh 3

def hitung_pangkat(angka,pangkat):
    hasil = angka**pangkat
    return hasil

a = hitung_pangkat(angka = 2, pangkat=3)
print(a)

# contoh 4

def fungsi(input1=1,input2=2,input3=3,input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil

print(fungsi())        # default
print(fungsi(input1=19))  # kalo ada yg mau di ganti