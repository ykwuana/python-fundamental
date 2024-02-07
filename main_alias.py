# lebih sederhana drpd 54-55.import dan module.py
# as = alias >>> bebas, suka2

from matematika import tambah as add
from matematika import kali as k
from matematika import pangkat as p

# import matematika as math # <<<<< bisa dilakukan
hasil_tambah = add(1,2,3,4,5)
print(f'hasil tambah = {hasil_tambah}')

hasil_kali = k(1,2,3,4,5)
print(f'hasil kali = {hasil_kali}')

pangkat_3 = p(3)
print(f'hasil pangkat 3 = {pangkat_3(2)}')
