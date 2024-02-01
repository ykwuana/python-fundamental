
import datetime
import string
import random


mahasiswa_template = {
    'nama' : 'nama',
    'nim' : '0000000',
    'sks_lulus' : 0,
    'lahir' : datetime.datetime(1111,1,11)
}

data_mahasiswa = {}

while True:

    print(f'{'SELAMAT DATANG':^20}')
    print(f'{'DATA MAHASISWA':^20}')
    print('-'*20)


    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa['nama'] = input('nama mahasiswa :')
    mahasiswa['nim'] = input('NIM Mahasiswa: ')
    mahasiswa['sks_lulus'] = input('SKS Lulus : ')
    tahun_lahir = int(input('Tahun Lahir (yyyy) : '))
    bulan_lahir = int(input('Bulan Lahir (1-12) : '))
    tanggal_lahir = int(input('Tanggal lahir (1-31) : '))
    mahasiswa['lahir'] = datetime.datetime(tahun_lahir,bulan_lahir,tanggal_lahir)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY:mahasiswa})

    print(f'\n{'Key':<8} {'Nama' :<17}{'Nim':<15}{'sks_lulus':<5}{'lahir':<12}')
    print('-'*50)

    for mahasiswa in data_mahasiswa:
        key = mahasiswa
        NAMA = data_mahasiswa[key]['nama']
        NIM = data_mahasiswa[key]['nim']
        SKS = data_mahasiswa[key]['sks_lulus']
        # BEASISWA = data_mahasiswa[key]['beasiswa']
        LAHIR = data_mahasiswa[key]['lahir'].strftime('%x')

        print(f'{key:<8}{NAMA:<17}{NIM:<11}{SKS:<6}{LAHIR:<10}')

    print('\n')
    is_done = input('sudah beres bro (y/n) ? ')
    if is_done == 'y':
        break

print('\nakhir dari program, terima kasih')
