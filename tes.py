"""
ibu berkata, "baca dan pahami semua bukumu"

jumlah buku yang sudah dibaca dan di pahami = 0
buku ke 1 sudah dibaca dan di pahami
buku ke 2 sudah dibaca dan di pahami
buku ke 3 sudah dibaca dan di pahami
buku ke 4 sudah dibaca dan di pahami
buku ke 5 sudah dibaca dan di pahami
buku ke 6 sudah dibaca dan di pahami
buku ke 7 sudah dibaca dan di pahami
buku ke 8 sudah dibaca dan di pahami
buku ke 9 sudah dibaca dan di pahami
buku ke 10 belum paham
buku ke 10 belum paham
buku ke 10 belum paham
buku ke 10 belum paham
buku ke 10 belum paham
buku ke 10 belum paham
buku ke 10 belum paham
buku ke 10 belum paham
buku ke 10 belum paham
buku ke 10 belum paham
buku ke 10 belum paham

jumlah buku yang sudah dibaca dan dipahami 9
bu, tidak semua buku bisa di pahami, budi hanya bisa memahami sebanyak 9 buku saja
"""

print(f'ibu berkata, "baca dan pahami semua bukumu')
jumlah_buku = 10

jumlah_buku_yang_sudah_dibaca_dan_dipahami = 0
print(f'jumlah buku yang sudah dibaca dan di pahami = {jumlah_buku_yang_sudah_dibaca_dan_dipahami}')

total_buku_yang_sudah_dibaca = 0

while total_buku_yang_sudah_dibaca < jumlah_buku * 2:
    total_buku_yang_sudah_dibaca += 1
    if jumlah_buku_yang_sudah_dibaca_dan_dipahami == 9:
        print(f'buku ke {jumlah_buku_yang_sudah_dibaca_dan_dipahami + 1} belum paham')

    else:
        jumlah_buku_yang_sudah_dibaca_dan_dipahami += 1
        print(f'buku ke {jumlah_buku_yang_sudah_dibaca_dan_dipahami} sudah dibaca dan di pahami')