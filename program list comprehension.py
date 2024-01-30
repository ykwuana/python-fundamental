# daftar_buku = [13, 73, 33,]
# # data.pop()
# # print(data)
# #
# # data_1 = data.pop(1)
# # print(data_1)
#
# # del data[:]  #start : stop : step
# #
# # # print(data)   # hasilnya [] dan kesamping
# #
# # for i in range(0, len(data)):        # hasilnya hilang semua dan ke bawah
# #     print(data[i])
#
# # membuat list baru
# print(('\nmembuat data baru'))
# daftar_buku_baru = daftar_buku[:]
# for i in range(0, len(daftar_buku)):
#     print(daftar_buku[i])
#
# # membuat list baru
# print(('\nmembuat data baru1'))
# del daftar_buku[:]
# for i in range(0, len(daftar_buku_baru)):
#     print(daftar_buku_baru[i])

data = [1,2,3,4,5,6,7,8,9]
data_baru = data[7::-2]

for i in range(0, len(data_baru)):
    print(data_baru[i])