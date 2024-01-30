# copy dictionary

teman_teman = {
    'cup' : 'ucup surucup',
    'tong' : 'otong surotong',
    'dung' : 'dung surudung',
    'sep' : 'asep si kasyep',
    'mar' : 'marimar',
}

friends = teman_teman
print(f'\nteman-teman = {teman_teman}')
print(f'friends = {friends}')

print(f'\n{5*'-'} di ubah valuenya maka dua2 nya ikut berubah juga {5*'-'}')
teman_teman['cup'] = 'ucup si kweren'
print(f'\nteman-teman = {teman_teman}')
print(f'friends = {friends}')

print(f'\n{5*'-'} cara nya biar gak ikut berubah juga maka ditambahkan copy {5*'-'}')
friends = teman_teman.copy()
teman_teman['cup'] = 'ucup si mantul'
print(f'\nteman-teman = {teman_teman}')
print(f'friends = {friends}')

#
print(f'\n{5*'-'} pop dictionary (berdasrkan key), mindahin data {5*'-'}')
data_asep = friends.pop('sep')
print(f'data asep = {data_asep}')
print(f'\n{5*'+'} data si "sep" sudah gk ada, sdh pindah dari friends ke data_asep {5*'+'}')
print(f'friends = {friends}')

#
print(f'\n{5*'-'} pop dictionary (yang terakhir aja), mindahin data {5*'-'}')
data_terkahir = friends.popitem()
print(f'data terakhir = {data_terkahir}')
print(f'friends = {friends}')


