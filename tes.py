import datetime

mahasiswa_1 = {
    'nama' : 'Ucup Surucup',
    'Nim' : '200041016',
    'jumlah_sks' : '130',
    'beasiswa' : False,
    'lahir' : datetime.datetime(1987,4,11)
}

mahasiswa_2 = {
    'nama' : 'Otong Surotong',
    'Nim' : '200041017',
    'jumlah_sks' : '140',
    'beasiswa' : True,
    'lahir' : datetime.datetime(1988,6,19)
}

mahasiswa_3 = {
    'nama' : 'Asep si Kasyep',
    'Nim' : '200041018',
    'jumlah_sks' : '100',
    'beasiswa' : False,
    'lahir' : datetime.datetime(1985,7,8)
}


print(f'{'KEY':<8}{'Nama':<17}{'NIM':<11}{'SKS':<6}{'Beasiswa':<10}{'Lahir':^10}')
print(f'{60*'-'}')

data_mahasiswa = {
    'MAH001' : mahasiswa_1,
    'MAH002' : mahasiswa_2,
    'MAH003' : mahasiswa_3,
}

for mahasiswa in data_mahasiswa:
    key = mahasiswa
    NAMA = data_mahasiswa[key]['nama']
    NIM = data_mahasiswa[key]['Nim']
    SKS = data_mahasiswa[key]['jumlah_sks']
    BEASISWA = data_mahasiswa[key]['beasiswa']
    LAHIR = data_mahasiswa[key]['lahir'].strftime('%x')

    print(f'{key:<8}{NAMA:<17}{NIM:<11}{SKS:<6}{BEASISWA:^10}{LAHIR:<10}')


