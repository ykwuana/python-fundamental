import datetime

mahasiswi1 = {
    'nama' : 'ucup surucup',
    'nim'  : '200041019',
    'sks_lulus' : 130,
    'beasiswa' : False,
    'lahir' : datetime.datetime(1987,4,10)
}

mahasiswi2 = {
    'nama' : 'otong surotong',
    'nim'  : '200041020',
    'sks_lulus' : 140,
    'beasiswa' : True,
    'lahir' : datetime.datetime(1986,5,15)
}

mahasiswi3 = {
    'nama' : 'Asep si Kasyep',
    'nim'  : '200041023',
    'sks_lulus' : 100,
    'beasiswa' : False,
    'lahir' : datetime.datetime(1989,2,28)
}

data_mahasiswa = {
    'MAH001' : mahasiswi1,
    'MAH002' : mahasiswi2,
    'MAH003' : mahasiswi3
}

print(f'{'Key':<8} {'Nama' :<17}{'Nim':<15}{'sks':<5}{'beasiswa':^9}{'lahir':<12}')
print('-'*50)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa

    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime('%x')

    print(f'{KEY:<8} {NAMA :<17}{NIM:<15}{SKS:<5}{BEASISWA:^9}{LAHIR:<12}')

