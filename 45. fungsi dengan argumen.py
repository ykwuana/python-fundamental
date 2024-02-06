''' Fungsi dengan argumen'''

# template
# def nama_fungsi (argumen)
# badan fungsi

def hello_world(nama):
    '''fungsi hello world  menerima input dengan varible nama'''
    print(f'selamat datang dunia wahai {nama}')

hello_world('ucup')
hello_world('asyep')

def tambah(angka_1,angka_2):
    hasil= angka_1 + angka_2
    print(f'{angka_1} + {angka_2} = {hasil}')

tambah(1,5)
tambah(100000,1)

def say_hi(list_peserta):
    # data_peserta = list_peserta.copy()   # aslinya pake ini tp blom tau kegunaannya
    list_peserta[1] = 'asyep'
    for peserta in list_peserta:
        print(f'yang terhormat {peserta}')

anggota_boyband = ['ucp', 'otong', 'dudung']

say_hi(anggota_boyband)

