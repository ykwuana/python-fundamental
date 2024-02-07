#
# # untuk menyambung program dari external
# import program_list
# # import main
#
# # import dengan data
# print(program_list.data_list)
#
# # import dengan fungsi
#
# hasil = program_list.tambah(4,5)
# print(hasil)
#
# module matematika dengan import

import matematika

hasil_tambah = matematika.tambah(1,2,3,4,5)
print(f'hasil tambah = {hasil_tambah}')

hasil_kali = matematika.kali(1,2,3,4,5)
print(f'hasil kali = {hasil_kali}')

pangkat_3 = matematika.pangkat(3)
print(f'hasil pangkat 3 = {pangkat_3(2)}')

