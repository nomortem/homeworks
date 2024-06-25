my_dict = {'Sergey' : 1985, 'Anton' : 1984, 'Sasha' : 1986, 'Jenya' : 1995}

print(my_dict)

print(my_dict.get('Sergey'))
print(my_dict.get('Denis'))

my_dict.update({'Dasha' : 1990})
my_dict['Nastya'] = 1988

a = my_dict.pop('Sasha')
print(a)

print(my_dict)

my_set = {1,2,3,3,2,1,'a', 'up',"a"}

print(my_set)

my_set.add(5)
my_set.add(6)

my_set.remove('up')

print(my_set)



