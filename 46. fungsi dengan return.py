# tujuan dari return agar lebih simpel misal : a atau b dst


def kuadrat(input_angka):
    output_kuadrat = input_angka**2
    return output_kuadrat

t = kuadrat(5)
print(t + 40)

# fungsi tambah

def fungsi_tambah(angka_1,angka_2):
    return angka_1 + angka_2

a = fungsi_tambah(7,8)
print(a)

# fungsi dengan return banyak

def operasi_matematika (angka_1,angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2

    return tambah,kurang,kali,bagi
k,l,m,n = operasi_matematika(125,5)

print(f'hasil tambah = {k}')
print(f'hasil kurang = {l}')
print(f'hasil kali = {m}')
print(f'hasil bagi = {n}')
