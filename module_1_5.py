immutable_var = (1, 's', True, 'aple')
print('Tuple:',immutable_var)
#immutable_var[0] = 2   #-В кортеж изщиенения не вносятся
mutable_list = [1, 's', True, 'aple']
print('List:',mutable_list)
mutable_list[0] = 2
mutable_list[2] = False
print('Modified List:',mutable_list)