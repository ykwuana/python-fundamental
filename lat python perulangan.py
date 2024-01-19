
"""""""
Perulangan :
1. for
2. break
3. continue
4. while
"""""""

# for i in range(1,6,2):
#     print('loop')

# for i in range(1,30,3):
#     if i == 25:
#         break
#     print(i)

# for i in range(1,30,3):
#     if i == 25:
#         continue
#
#     print(i)

# print angka ganjil dari 1 sampai 10
# cara 1

# for i in range(1,10):
#     if i%2 == 0:
#         continue
#     print(i)

# cara 2

# for i in range(1,10):
#     if i%2 != 0:
#         print(i)

# while statement

jumlah_uang = 10000

while(jumlah_uang>0):
    print('sisa uang di dompet tinggal ' + str(jumlah_uang))
    jumlah_uang -= 1000

print('waduh,uangku sudah habis toh')

done