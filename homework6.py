my_dict = {'Irina': 1986, 'Semen': 1987, 'Bogdan': 2019, 'Danil': 2011}
print('Dict:', my_dict)
print('Existing value:', my_dict['Bogdan'])
print('Not existing value:', my_dict.get('Denis'))
my_dict.update({'Stepan': 2010, 'Lera': 2009})
a = my_dict.pop('Danil')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)

my_set = {1, 2, 3, 'www', 3, 2.2, 'url', 'www'}
print('Set:', my_set)
my_set.update([5, 'http'])
my_set.discard('www')
print('Modified set:', my_set)