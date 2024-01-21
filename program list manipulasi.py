## Operasi

# index  0(-3)     1(-2)    2(-1)
data = ["ucup", "otong", "dudung"]

 # mengambil data dari list ini
data_0 = data[0]
print(f'data pertama (index 0) = {data_0}')

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f'panjang data = {panjang_data}')

# menambahkan item pada list sesuai posisi
print(f'data sebelum ditambah = {data}')

data.insert(1,'asep')                #(posisi,item)
print(f'data setelah ditambah = {data}')

# nambahnya langsung di akhir list
data.append('jajang')
print((f'data ditambah lagi = {data}'))

# menambah list dengan list
data_baru = ['ujang', 'usep', 'dadang']
data.extend(data_baru)
print(f'data gabungan {data}')

# merubah data
data[2] = 'michael'
print(f'data rubah = {data}')

# me remove data
data.remove('ujang')
print(f'data remove {data}')

# meremove data paling akhir
data_akhir = data.pop()  # bisa juga langsung spt >>>>> data.pop()>>>>>>tapi ini untuk pop aj
print(f'data akhir diremove {data}')

print(f'nama akhir yang di hapus = {data_akhir}')
