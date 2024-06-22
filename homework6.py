my_dict = {'Anton' : 1925, 'kirill' : 1933, 'Alesha' : 1919, 'Doljen_babki' : 1940}
print(my_dict)
print(my_dict['Anton'])
print(my_dict.get('Foma'))
my_dict.update({'Tamara' : 1927 , 'Ilya' : 1918})
a = my_dict.pop('Alesha')
print(a)
print(my_dict)


my_set = {1, 2, 3, 'You', 'You', 1, 4, 5, False}
print(my_set)
my_set.add((1, 2, 3))
my_set.add('Privet')
my_set.remove(False)
print(my_set)

