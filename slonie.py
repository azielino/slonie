n = 11
mass_list = [4735, 5525, 4720, 3648, 3280, 3726, 4684, 5959, 3797, 3181, 3585]
start_list = [4, 11, 6, 5, 2, 3, 10, 7, 9, 8, 1]
end_list =   [11, 8, 6, 1, 5, 4, 9, 2, 3, 10, 7]

def assign_elephant(list):
    return {nr : mass for nr, mass in enumerate(list, 1)}

def format_list(list):
    return [nr - 1 for nr in list]

start_list_0 = format_list(start_list)
end_list_0 = format_list(end_list)
elephants = assign_elephant(mass_list)
min_all = min(mass_list)
permutation = {}
check_list = []

for i in range(n):
    # Konstrukcja permutacji
    permutation[end_list_0[i]] = start_list_0[i]
    # Rozkład na cykle proste
    check_list.append(False) 
cycles = {}
c = 0
for i in range(n):
    if not check_list[i]:
        c += 1
        cycles[c] = []
        x = i 
        while not check_list[x]:
            check_list[x] = True
            x = permutation[x]
            cycles[c].append(x + 1)
print(cycles)
# Wyznaczenie parametrów cykli
suma_c = {}
min_c = {}
for i in range(1, c + 1):
    suma_c[i] = 0
    min_c[i] = 0
    elephants_c = []
    for e in cycles[i]:
        suma_c[i] += elephants[e]
        elephants_c.append(elephants[e])
    min_c[i] = min(elephants_c)
print(min_all)
print(suma_c)
print(min_c)
# Obliczenie wyniku
w = 0
metoda1 = {}
metoda2 = {}
for i in range(1, c + 1):
    metoda1[i] = suma_c[i] + ((len(cycles[i]) - 2) * min_c[i])
    print(f'metoda1[{i}]: {metoda1[i]}')
    metoda2[i] = suma_c[i] + min_c[i] + ((len(cycles[i]) + 1) * min_all)
    print(f'metoda2[{i}]: {metoda2[i]}')
    w += min(metoda1[i], metoda2[i])
print(w)
