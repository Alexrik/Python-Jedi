#def test():
#	print ('test')

#az = test()
#print (az) этот print выведет None так как функция test
		  #  ничего не возвращает

diction = {
	"key1" : "value1",
	"key2" : "value2",
	"key4" : (1, 2, 3) # в качестве значения элементов словоря					   
					   # могут выступать любые типы данных
}

print (diction["key1"])

try:
	print (diction["key_some"])
except KeyError:
	print ('Such a key does not exist')

print (diction.get("key52", "not found")) # отличие конструкции с get от обычной
							# в том что .get может принять второе значение

#if "key4" in diction:
#	print ('yes')
#else:
#	print ('no') # полезно для поиска в словаре

contacts = {
	'Alex' : '+23456767',
	'Rob' : '+20984756',
	'Nick' : '+34506900'
}

search = input ('Who you want to find? ')

if search in contacts:
	print ('His number is -- ' + contacts[search])
else:
	print ('We have no ' + search + '\'s number')
