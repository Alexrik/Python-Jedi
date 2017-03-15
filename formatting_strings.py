person_name = 'Alex'
person_age = 22

# %
# .format()

#print('Hello, %s!\nYour are already %d years old' %(name, age))

#print ('Hello, {name}!\nYou are already {age} years old'.format(name = person_name, age = person_age))

#print ('{0}{1}{0}'.format('habr', 'a')) # в функции .format присутствует индексирование

human = {
	'name' : 'Alex',
	'age' : 22
}

#print ('Name: {person[name]}\nAge: {person[age]}'.format (person = human))

# программа кладет введенное значение посредине заполнителя *
input_str = input ('Input some name: ')
length = 10

if len(input_str) % 2:
	length += 1
	
print (('{0:*^' + str(length) +'}').format (input_str))

#print (len(input_str))

#print ('{0:*^12}'.format (input_str))