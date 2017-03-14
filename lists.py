list_1 = [1, 2, 3, 4, 5]

list_1.reverse()
#print (max(list_1))
#print (min(list_1))
#print (list_1.count(1))
#print (list_1)

list_2 = [1, 2, 3]

#print (list_2 * 2)

list_3 = [1, 2, 3]

#print (list_3 + [4, 5])

string = 'hello'

#print (string[4]) 

name_list = ['Alex', 'Rob', 'Nick']

#if 'alex' in names:
#	print('alex is in list')# так же с числами

#---------------------пополняем список динамично


name_list.append ('John')
name_list.append ('Piter')
name_list.append ('Bob')
name_list.insert (1, 'Bill')

print (name_list)

#name_list.remove ('Bob') удаляет элемент из списка
name_list.insert (0, 5)

if len(name_list) <= 4:
	print ('В списке name_list находится ' + str(len(name_list)) + ' элемента' )
else:
	print ('В списке name_list находится ' + str(len(name_list)) + ' элементов')

passW = 'jedimaster'

name = input ('Your name: ')
password = input ('Password: ')
if name in name_list and passW == password:
	print('hello, ' + name + ' wellcome!')
elif name in name_list and passW != password:
	print('write correct password ' + name + '!')
	password = input('Password: ')
	if password == passW:
		print('hello, ' + name + ' wellcome!')
else:
	print('Who are you ' + name + '?') 