# cara lain untuk output list nya
print(25*'=')
print('cara alternatif untuk output list')
print(25*'=' + '\n')

list_example = [30, 33, 50, 75, 40, 77, 60, 55]
for item in list_example:
    print(item)
print('\n' + 5*'+' + ' ATAU ' + 5*'+')

for unit in range(0, len(list_example)):   # ini dipake kalo datanya urutan tertentu
    print(list_example[unit])              # misal dari urutan 3 sd 10 atau 3 sd akhir

#atau buat cari yang genap
print(25*'=')
print('untuk mencari yang genap')
print(25*'=' + '\n')

for angka in list_example:
    if angka % 2 == 0:
        print(f'{angka}\n')

# atau untuk mencari item tertentu
print(25 * '=')
print('untuk mencari item tertentu')
print(25 * '=' + '\n')


if 33 in list_example:
    print(f'ada angka 33 di list example = {33}\n')             # kalo gk ada itemnya, gk keluar angkanya

# untuk copy list dengan identity yg berbeda

print(25 * '=')
print('untuk copy list dengan identity yg berbeda')
print(25 * '=' + '\n')

data_list_1 = [60, 20, 30, 15, 27, 9]
data_list_2 = data_list_1.copy()
data_list_2.insert(3, 77)
data_list_2[4] = 13                        # di ganti
print(data_list_1)
print(data_list_2)

# untuk mengurutkan
print(25*'=')
print('untuk mengurutkan')
print(25*'=' + '\n')

data_list_2.sort()
print(f'setelah diurutkan = {data_list_2}\n')

# untuk dibalik
print(25*'=')
print('untuk di balik')
print(25*'=' + '\n')

data_list_2.reverse()
print(f'setelah dibalik = {data_list_2}\n')

data_list_2.remove(0)
print(data_list_2)