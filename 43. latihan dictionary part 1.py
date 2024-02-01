
import datetime
import string
import random


mahasiswa_template = {       # create 1
    'nama' : 'nama',         # data2 apa aja yg akan dimasukkan
    'nim' : '0000000',
    'sks_lulus' : 0,
    'lahir' : datetime.datetime(1111,1,11)
}

data_mahasiswa = {}  # sengaja di buat walaupun kosong


print(f'{'SELAMAT DATANG':^20}')
print(f'{'DATA MAHASISWA':^20}')
print('-'*20)

while True:

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
                      # create 2 (mahasiswa template masuk sini)
                      # jadi inputan nya sesuai dengan create 1
    mahasiswa['nama'] = input('nama mahasiswa :')
    mahasiswa['nim'] = input('NIM Mahasiswa: ')
    mahasiswa['sks_lulus'] = input('SKS Lulus : ')
    tahun_lahir = int(input('Tahun Lahir (yyyy) : '))
    bulan_lahir = int(input('Bulan Lahir (1-12) : '))
    tanggal_lahir = int(input('Tanggal lahir (1-31) : '))
    mahasiswa['lahir'] = datetime.datetime(tahun_lahir,bulan_lahir,tanggal_lahir)

    kode = ''.join((random.choice(string.ascii_uppercase) for i in range(5)))
    # create 3

    data_mahasiswa.update({kode:mahasiswa})
            # create 4 >>> create 3 + 2 masuk sini
            # jadi ceritanya adalah data_mahasiswa ditambah kode untuk per mahasiswa.
    print(f'\n{'Kode':<8} {'Nama' :<17}{'Nim':<15}{'sks_lulus':<12}{'lahir':<12}')
    print('-'*50)

    for siswa in data_mahasiswa:
        ab = siswa
        NAMA = data_mahasiswa[ab]['nama']
        NIM = data_mahasiswa[ab]['nim']
        SKS = data_mahasiswa[ab]['sks_lulus']
        # BEASISWA = data_mahasiswa[key]['beasiswa']
        LAHIR = data_mahasiswa[ab]['lahir'].strftime('%x')

        print(f'{ab:<8}{NAMA:<17}{NIM:<15}{SKS:^9}{LAHIR:<12}')

    print('\n')
    is_done = input('sudah beres bro (y/n) ? ')
    if is_done == 'y':
        break

print('\nakhir dari program, terima kasih')
