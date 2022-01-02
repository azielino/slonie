import sys

data_file_name = sys.argv[1]
with open(f'zadanie_B/{data_file_name}') as file:
    str_data_list = file.readlines()

def str_list_to_int_list(list):
    return [int(item.replace('\n', '')) for item in list]

n = int(str_data_list[0].replace('\n', ''))
mass_list = str_list_to_int_list(str_data_list[1].split(' '))
start_list = str_list_to_int_list(str_data_list[2].split(' '))
end_list = str_list_to_int_list(str_data_list[3].split(' '))

def assign_elephant_mass(list):
    return {nr : mass for nr, mass in enumerate(list, 1)}

def format_elephant_nr(list):
    return [elephant_nr - 1 for elephant_nr in list]

start_list_0 = format_elephant_nr(start_list)
end_list_0 = format_elephant_nr(end_list)
elephants = assign_elephant_mass(mass_list)
min_all = min(mass_list)
permutation = {}
check_list = []
cycles = {}
c = 0
sum_c = {}
min_c = {}
method1 = {}
method2 = {}
result = 0
# ----------------------------- Konstrukcja permutacji
for i in range(n):
    permutation[end_list_0[i]] = start_list_0[i]
    check_list.append(False)
# ----------------------------- Rozkład na cykle proste
for i in range(n):
    if not check_list[i]:
        c += 1
        cycles[c] = []
        x = i 
        while not check_list[x]:
            check_list[x] = True
            x = permutation[x]
            cycles[c].append(x + 1)
# ----------------------------- Wyznaczenie parametrów cykli
# ----------------------------- Obliczenie wyniku
for i in range(1, c + 1):
    sum_c[i] = 0
    min_c[i] = 0
    elephants_c = []
    if len(cycles[i]) > 1:
        for e in cycles[i]:
            sum_c[i] += elephants[e]
            elephants_c.append(elephants[e])
        min_c[i] = min(elephants_c)
        method1[i] = sum_c[i] + ((len(cycles[i]) - 2) * min_c[i])
        if min_c[i] != min_all:
            method2[i] = sum_c[i] + min_c[i] + ((len(cycles[i]) + 1) * min_all)
            result += min(method1[i], method2[i])
        else:
            result += method1[i]
print(result)