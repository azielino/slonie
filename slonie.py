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

permutation = {}
check_list = []
for i in range(n):
    permutation[end_list0[i]] = start_list0[i]
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

