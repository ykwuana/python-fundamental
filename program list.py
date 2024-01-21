## cara alternatif membuat list
data_range = range(0,10,3)

data_list = list(data_range)
print(data_list)

# membuat list dengan for loop, list comprehensip
list_pake_for = [i for i in range(0,10)]
print(list_pake_for)

list_pake_for = [i**2 for i in range(0,10)]   # ditambah**2 dibacanya kuadrat 2
print(list_pake_for)

# membuat list pake for pake if
list_pake_for_if = [i for i in range(0,10) if i != 5]    #jika i tidak sama dengan 5 (5 nya hilang)
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0,10) if i%2 == 0]    # genap
print(list_pake_for_if)

list_pake_for_if = [i**2 for i in range(0,10) if i%2 != 0]    # ganjil kuadrat
print(list_pake_for_if)