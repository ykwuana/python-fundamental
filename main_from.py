# lebih sederhana drpd 54-55.import dan module.py

from matematika import tambah,kali,pangkat
# from matematika import * # atau ini bisa dipakai kalo mau borong semua
                        # hanya saja takut bingunng kala tambah ambil nya dari modul yg mana

hasil_tambah = tambah(1,2,3,4,5)
print(f'hasil tambah = {hasil_tambah}')

hasil_kali = kali(1,2,3,4,5)
print(f'hasil kali = {hasil_kali}')

pangkat_3 = pangkat(3)
print(f'hasil pangkat 3 = {pangkat_3(2)}')
