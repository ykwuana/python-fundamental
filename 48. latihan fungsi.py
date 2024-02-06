# #
# # print(f'{'PROGRAM MENGHITUNG LUAS' :^40}')
# # print(f'{'DAN KELILING PERSEGI PANJANG' :^40}')
# # print(f'{'-'*40 :^40}')
# #
# # # mengambil input user
# #
# # panjang = int(input('masukkan nilai panjang = '))
# # lebar = int(input('masukkan nilai lebar = '))
# #
# # # program menghitung luas
# #
# # luas = panjang*lebar
# # keliling = 2*(panjang+lebar)
# #
# # # tampilkan hasilnya
# # print(f'hasil perhitungan luas = {luas}')
# # print(f'hasil perhitungan keliling = {keliling}')
#
def header():
    print(f'{'PROGRAM MENGHITUNG LUAS' :^40}')
    print(f'{'DAN KELILING PERSEGI PANJANG' :^40}')
    print(f'{'-' * 40 :^40}')


def input_user():
    '''fungsi input user'''
    # mengambil input user
    lebar = int(input('masukkan nilai lebar = '))
    panjang = int(input('masukkan nilai panjang = '))

    return lebar, panjang

def hitung_luas (lebar,panjang) :
    return lebar*panjang

def hitung_keliling (lebar,panjang) :
    return 2*(lebar+panjang)

def display (pesan,nilai):
    print(f'hasil perhitungan {pesan} = {nilai}')

# program utamanya
# while True:
#     header()
#
#     a,b = input_user()
#     luas = hitung_luas(a,b)
#     keliling = hitung_keliling(a,b)
#
#     display('luas', luas)
#     display('keliling', keliling)
#
#     iscontinue = input('apakah lanjut (y/n) :')
#     if iscontinue == 'n':
#         break
#
# print('program selesai, terimakasih')
header()
while True :
    opsi = input('anda ingin menghitung luas atau keliling (luas=1 / keliling=2) : ')
    if opsi == '1':
        a, b = input_user()
        luas = hitung_luas(a,b)
        display('luas', luas)
    elif opsi == '2':
        a,b =input_user()
        keliling = hitung_keliling(a, b)
        display('keliling',keliling)

    elif opsi != '1' or opsi !='2':
        print('anda blom masukkan opsi atau opsi anda tidak sesuai')

    iscontinue = input('apakah lanjut (y/n) :')
    if iscontinue == 'n':
        break
print('\nPROGRAM SELESAI')

