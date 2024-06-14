my_dict = { 'Sergey': 2005, 'Dmitriy':2001, 'Roman':2004 }

print('Dict: ', my_dict)
print('Exicting value: ', my_dict['Sergey'])
my_dict['Anton'] = 1999
print('Not Existing value: ', my_dict['Anton'])
my_dict.update({'Bob':2005,
                'James':1965})
a = my_dict.pop('Anton')
print('Deleted Value: ', a)
print('Modifed dict: ', my_dict)

print(" ")

my_set = {1, 2, 3, 4, 5, 1, 2, 3, 4}
print('Set: ', my_set)
my_set.add(6)
my_set.add(7)
my_set.remove(4)
print('Modifed Set', my_set)



