# looping dictionary

teman_teman = {
    'cup' : 'ucup surucup',
    'tong' : 'otong surotong',
    'dung' : 'dung surudung',
    'sep' : 'asep si kasyep',
    'mar' : 'marimar',
}

print(f'\n{5*'+'} looping first try {5*'+'}')

for teman in teman_teman:     #versi list, yg keluar key
    print(teman)

#
print(f'\n{5*'+'} operator untuk mengambil item / iterables {5*'+'}')
keys = teman_teman.keys()
print(keys)

print(f'\n{5*'+'} atau 1 untuk mengambil keynya {5*'+'}\n')
for key in teman_teman.keys():
    print(key)

print(f'\n{5*'+'} atau 2 untuk mengambil value nya{5*'+'}\n')
for key in teman_teman.keys():
    print(teman_teman.get(key))

print(f'\n{5*'+'} atau 3 untuk mengambil value nya {5*'+'}\n')
values = teman_teman.values()
print(values)

print(f'\n{5*'+'} atau 4 untuk mengambil value nya {5*'+'}\n')   # bandingannya di atau 1
for values in teman_teman.values():
    print(values)

print(f'\n{5*'+'} atau 5 untuk mengambil itemnya {5*'+'}\n')
items = teman_teman.items()
print(items)

print(f'\n{5*'+'} atau 6 untuk mengambil itemnya {5*'+'}\n')
for item in teman_teman.items():
    print(item)

print(f'\n{5*'+'} atau 6 untuk mengambil itemnya {5*'+'}\n')
for a,b in teman_teman.items():
    print(f'key = {a}, value = {b}')



