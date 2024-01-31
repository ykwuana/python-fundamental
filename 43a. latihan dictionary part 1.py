
import datetime

mahasiswa_template = {
    'nama' : 'nama',
    'nim' : '0000000',
    'sks_lulus' : 0,
    'lahir' : datetime.datetime(1111,1,11)
}

data_mahasiswa = {}

mahasiswa = dict.fromkeys(mahasiswa_template.keys())
mahasiswa['nama'] = input('nama mahasiswa :')
print(mahasiswa)

