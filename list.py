family = ['sampson', 'micah', 'imoh', 'faith']
family.append('Endurance')
print(family)
midle = len(family) //2

sublist = family[midle:]
sublist.sort()
family[midle:] = sublist
print(family)

moreNames = ['Zuriel', 'Micheal', 'clowes']
family.extend(moreNames)
print(family)

family.insert(4, 'clopathra')
print(family)

family.pop(4)
print(family)

family.remove('clowes')
print(family)
