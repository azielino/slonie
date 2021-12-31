n = 6
mass_list = [2400, 2000, 1200, 2400, 1600, 4000]
start_list = [1, 4, 5, 3, 6, 2]
end_list =   [5, 3, 2, 4, 6, 1]

def elephants_mass(list):
    elephants = {}
    for nr, mass in enumerate(list):
        elephants[nr + 1] = mass
    return elephants

def format_list_numeration(list):
    list0 = []
    for nr in list:
        nr -= 1
        list0.append(nr)
    return list0

start_list0 = format_list_numeration(start_list)
end_list0 = format_list_numeration(end_list)

elephants = elephants_mass(mass_list)
print(elephants)

permutation = {}
check_list = []
for i in range(n):
    permutation[end_list0[i]] = start_list0[i] # Konstrukcja permutacji
    check_list.append(False) # Rozkład na cykle proste
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
min_all = int
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
print(suma_c)
print(min_c)

# Obliczenie wyniku


