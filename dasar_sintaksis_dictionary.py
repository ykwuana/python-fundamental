#
# users = {
#     'id' : 1,
#     'name' : 'leanne graham',
#     'username' : 'bret',
#     'email' : 'sincere@april.biz'
# }
# print(users)
# print(users['id'])
# print(users['name'])
# print(users['username'])
# print(users['email'])

data_list = ['ucup', 'otong', 'dudung']
data_dict = {
    'nmbr' : 100,
    'list' : data_list,   # kalo dikasih tanda petik outputnya [data_list]
}
print(data_list)
print(data_dict['nmbr'])
print(data_dict['list'])

# Operator dictionary
print(f'\n{5*'+'} panjang dictionary {5*'+'}')

data_dict = {
    'cup' : 'ucup surucup',
    'tong' : 'otong surotong',
    'dung' : 'dung surudung',
    'mar' : 'marimar'
}
#
lendict = len(data_dict)
print(f'panjang data dict = {lendict}')

#
print(f'\n{5*'+'} mengecek key exist atau tidak {5*'+'}')

KEY = 'cup'
CHECKKEY = KEY in data_dict
print(f'apakah {KEY} ada di data_dict = {CHECKKEY}')

#
print(f'\n{5*'+'} mengakses value (read) dengan get {5*'+'}')

print(data_dict['cup'])  # versi tanpa get
print(data_dict.get ('cup')) # versi dengan get

print(data_dict.get('kis'))  # kalo bukan versi get akan error hasilnya, karena tidak ada
print(data_dict.get('kis', 'key tidak ditemukan')) # dan di versi get kalo tidak ada,
                                                   # output none nya bisa di edit kata2nya

#
print(f'\n{5*'+'} mengupdate data {5*'+'}')
data_dict['cup'] = 'ucup si ganteng'
print(data_dict)
data_dict['sep'] = 'asep si kasyep'
print(data_dict)
# kalo sep nya sdh ada caranya gmn??

data_dict.update({'cup' : 'ucup surantap'}) # bisa meng update yang sudah ada atau kalo blom ada maka ditambah
print(data_dict)

#
print(f'\n{5*'+'} mendelete data pada dictionary  {5*'+'}')
del data_dict['tong']
print(data_dict)
