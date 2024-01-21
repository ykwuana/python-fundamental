# # #
# # # """""""
# # # Perulangan :
# # # 1. for
# # # 2. break
# # # 3. continue
# # # 4. while
# # # """""""
# # #
# # # # for i in range(1,6,2):
# # # #     print('loop')
# # #
# # # # for i in range(1,30,3):
# # # #     if i == 25:
# # # #         break
# # # #     print(i)
# # #
# # # # for i in range(1,30,3):
# # # #     if i == 25:
# # # #         continue
# # # #
# # # #     print(i)
# # #
# # # # print angka ganjil dari 1 sampai 10
# # # # cara 1
# # #
# # # # for i in range(1,10):
# # # #     if i%2 == 0:
# # # #         continue
# # # #     print(i)
# # #
# # # # cara 2
# # #
# # # # for i in range(1,10):
# # # #     if i%2 != 0:
# # # #         print(i)
# # #
# while statement

jumlah_uang = 10000

while(jumlah_uang>0):
    print(f'sisa uang di dompet tinggal  {jumlah_uang:,}')
    jumlah_uang -= 1000

print('waduh,uangku sudah habis toh')
# # #
# # # done
# #
# # for i in range(1,11):
# #     print(f"buku ke-{i} sudah dibaca ")
#
# data_str = 'saya ganteng habis'
#
# for i in data_str:
#     print(i)

# contoh dari udemy

# jumlah_buku = 11
# print(f'ibu berkata, "baca semua bukumu"')
#
# jumlah_buku_yang_sudah_dibaca = 0
#
# for jumlah_buku_yang_sudah_dibaca in range (1,jumlah_buku+1):
#     print(f'buku ke {jumlah_buku_yang_sudah_dibaca} sudah dibaca')
#
# print(f'\njumlah buku yang sudah di baca = {jumlah_buku_yang_sudah_dibaca}')