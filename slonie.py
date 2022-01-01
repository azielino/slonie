import sys

data_file = sys.argv[1]
data = []
with open(f'zadanie_B/{data_file}') as file:
    data_str_list = file.readlines()
for item in data_str_list:
    data.append(item.replace('\n', ''))

def list_str_to_list_int(list):
    return [int(item) for item in list]

n = int(data[0])
mass_list = list_str_to_list_int(data[1].split(' '))
start_list = list_str_to_list_int(data[2].split(' '))
end_list = list_str_to_list_int(data[3].split(' '))

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
# Konstrukcja permutacji
for i in range(n):
    permutation[end_list_0[i]] = start_list_0[i]
    check_list.append(False)
# Rozkład na cykle proste
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
# Obliczenie wyniku
w = 0
metoda1 = {}
metoda2 = {}
m1 = 0
m2 = 0
for i in range(1, c + 1):
    if len(cycles[i]) > 1:
        metoda1[i] = suma_c[i] + ((len(cycles[i]) - 2) * min_c[i])
        if min_c[i] != min_all:
            metoda2[i] = suma_c[i] + min_c[i] + ((len(cycles[i]) + 1) * min_all)
            w += min(metoda1[i], metoda2[i])
            if min(metoda1[i], metoda2[i]) == metoda1[i]:
                m1 += 1
            else: 
                m2 += 1
        else:
            w += metoda1[i]
            m1 += 1

print(w)

# testy
c1 = 0
for key, value in cycles.items():
    if len(value) == 1:
        c1 += 1

# print(n, c1, m1, m2)
