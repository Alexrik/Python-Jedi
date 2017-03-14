def string (name):
	''' описание функции'''
	print ('Hello, ' + name)

#print(string.__doc__) .__doc__ возвращает нам 'описание функции'

#my_var = string
#my_var() функцию можно прировнять к переменной

def read_name():
	return '===' + input('your rang: ') + '==='

string (read_name) #python может принимать в качестве аргумента другую функцию

