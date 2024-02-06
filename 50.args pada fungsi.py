

def fungsi(nama,tinggi,berat):
    print(f'{nama} punya tinggi {tinggi} dan berat {berat}')

fungsi('dudung',170,60)

def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f'{nama} punya tinggi {tinggi} dan berat {berat}')

fungsi(['otong',120,45])

# kenalan dengan *args

def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f'{nama} punya tinggi {tinggi} dan berat {berat}')

fungsi('ucup',145,65)

# studi kasus

def tambah(*data):
    # dengan * ini maka inputannya bebas mau berapa aja
    #data tipenya adalah tuple, dia bisa di iterasi
    output = 0
    for angka in data:
        output += angka
    return output




hasil = tambah(1,2,3,4,5,6,7,8,9)
print(hasil)

hasil = tambah(12,18,19,67,56,4,9,3,4,5,6,7,7,8)   # bebas mau brp aja
print(hasil)