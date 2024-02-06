# lambda function

def f_kuadrat(angka):
    return angka**2
print(f'hasil fungsi kuadrat = {f_kuadrat(3)}')

# kita coba dengan lambda
# output = lambda argument: expression
kuadrat = lambda angka:angka**2
print(f'hasil dari lambda kuadrat = {kuadrat(5)}')

# pangkat
pangkat = lambda a,b : a**b
print(f'hasil lambda pangkat = {pangkat(4,2)}')

# kegunaannya
# sorting untuk list

data_list = ['otong', 'ucup', 'dudung']
data_list.sort()
print(f'sorted list : {data_list}')

# sorting berdasarkan panjang hurufnya
data_list.sort(key=len)
print(f'sorted list by len : {data_list}')

# sorting berdasarkan panjang hurufnya pakai def
def panjang_nama(nama):
    return len(nama)
data_list.sort(key=panjang_nama)
print(f'sorted list by panjang_nama : {data_list}')

# sorting berdasarkan panjang hurufnya pakai lambda
data_list = ['otong', 'ucup', 'dudung']
data_list.sort(key=lambda a:len(a))
print(f'sorted list by lambda : {data_list}')

# filter
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]

# def kurang_dari_lima(angka):
#     return angka< 5
#
# data_angka_baru = list(filter(kurang_dari_lima,data_angka))
data_angka_baru_lambda = list(filter(lambda x:x<7,data_angka))

# print(data_angka_baru)
print(data_angka_baru_lambda)

# Genap
data_genap = list(filter(lambda x:(x%2==0),data_angka))
print(data_genap)

# ganjil
data_ganjil = list(filter(lambda x:(x%2!=0),data_angka))
print(data_ganjil)

# kelipatan 3
data_kelipatan_3 = list(filter(lambda x:(x%3==0),data_angka))
print(data_kelipatan_3)

# anonymous function
def pangkat(angka,n):
    return angka**n

hasil = pangkat(5,2)
print(f'dari fungsi biasa = {hasil}')

# dengan currying menjadi

def pangkat(n):
    return lambda angka:angka**n

pkt4 = pangkat(4)
print(f'pangkat2 = {pkt4(2)}')
         #atau
print(f'pangkat bebas = {pangkat(3)(2)}')