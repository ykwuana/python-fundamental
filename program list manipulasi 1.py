## Operasi

# index 0(-3)     1(-2)    2(-1)
data = ["ucup", "otong", "dudung"]

 # mengambil data dari list ini
print(25*'=')
print('untuk mengambil data dari list ini')
print(25*'=' + '\n')
data_0 = data[0]
print(f'data pertama (index 0) = {data_0}')

print(f'\n{10*'+'} ATAU {10*'+'}\n')
print(f'nama ucup ada diurutan ke = {data.index('ucup')}\n ')



# mengambil info jumlah data dalam list
print(25*'=')
print('untuk mencari berapa panjang/jumlah data')
print(25*'=' + '\n')

panjang_data = len(data)
print(f'panjang data = {panjang_data}\n')

# menambahkan item pada list sesuai posisi
print(25*'=')
print('untuk menambah data')
print(25*'=' + '\n')

print(f'data sebelum ditambah = {data}')

data.insert(1,'asep')                #(posisi,item)
print(f'data setelah ditambah = {data}\n')

# nambahnya langsung di akhir list
print(25*'=')
print('untuk menambah data di akhir list')
print(25*'=' + '\n')

data.append('jajang')
print((f'data ditambah lagi = {data}\n'))

# menambah list dengan list
print(25*'=')
print('untuk menambah list dengan list')
print(25*'=' + '\n')

data_baru = ['ujang', 'usep', 'dadang']
data.extend(data_baru)
print(f'data gabungan {data}\n')

# merubah data
print(25*'=')
print('untuk merubah data')
print(25*'=' + '\n')

data[2] = 'michael'
print(f'data rubah = {data}\n')

# me remove data
print(25*'=')
print('untuk meremove salah satu data')
print(25*'=' + '\n')

data.remove('ujang')
print(f'data remove {data}\n')



# meremove data paling akhir
print(25*'=')
print('untuk meremove data paling akhir')
print(25*'=' + '\n')

data_akhir = data.pop()  # bisa juga langsung spt >>>>> data.pop()>>>>>>tapi ini untuk pop aj
print(f'data akhir diremove {data}') # tapi bisa juga ditentukan urutan ke beberapa dengan mengisi urutan di []
                                                           # misal : data.pop(1)
print(f'nama akhir yang di hapus = {data_akhir}\n')

#untuk menghapus data yang di tuju
print(25*'=')
print('untuk menghapus data yang di tuju')
print(25*'=' + '\n')

del data[0]
print(f'{data}\n')

#untuk meghapus semua data
print(25*'=')
print('untuk meghapus semua data')
print(25*'=' + '\n')

data.clear()
print(f'{data}')