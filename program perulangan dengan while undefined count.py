"""
program perulangan membaca buku dengan while sampai paham
"""




jumlah_buku = 10
print(f'ibu berkata, "baca dan pahami semua bukumu"')

jumlah_buku_yang_sudah_dibaca_dan_dipahami = 0
total_jumlah_baca = 0
print(f'\njumlah buku yang sudah dibaca dan di pahami = {jumlah_buku_yang_sudah_dibaca_dan_dipahami}')

while total_jumlah_baca < jumlah_buku * 2:
    total_jumlah_baca += 1
    if jumlah_buku_yang_sudah_dibaca_dan_dipahami == 9:
        print(f'buku ke {jumlah_buku_yang_sudah_dibaca_dan_dipahami + 1} belum paham')

    else:
        jumlah_buku_yang_sudah_dibaca_dan_dipahami += 1
        print(f'buku ke {jumlah_buku_yang_sudah_dibaca_dan_dipahami} sudah dibaca dan di pahami')

print(f'\njumlah buku yang sudah dibaca dan dipahami {jumlah_buku_yang_sudah_dibaca_dan_dipahami} ')
if jumlah_buku_yang_sudah_dibaca_dan_dipahami == jumlah_buku:
    print('bu, semua buku sudah dibaca dan di pahami')

else:
    print(f'bu, tidak semua buku bisa di pahami, '
          f'budi hanya bisa memahami sebanyak {jumlah_buku_yang_sudah_dibaca_dan_dipahami} buku saja')
