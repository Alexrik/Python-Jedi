# ImportError ошибка импорта библиотеки
# IndexError ошибка доступа к несуществующим ячейкам
# NameError ошибка использования неинициализированной переменной
# SyntaxError ошибка синтаксиса
# TypeError ошибка передачи несовместимого аргумента функции
# ValueError ошибка значения переменной
# распостраненные виды исключений

#try:
	#eval ('print(7 / 4)a')
#	print(7 / 0)
#except:
#	raise

#except (ZeroDivisionError, NameError, TypeError, ValueError): # исключения можно
#	print ('stop it!')										  # перечислять через ','	


#except ZeroDivisionError:
#	print ('zero division!')

#except NameError:
#	print ('invalid variable')

#except SyntaxError:
#	print ('Syntax Error!') #python не может поймать SyntaxError без eval

#except:
#	print ('error')

#finally:
#	print ('stop errors')


#weather = 'bad'
#if weather == 'bad':
#	raise TypeError ('some information')
#except TypeError:
#	print('Type Error catched') # таким образом можно описать
								# свое исключение

#print ('program stop')

# ---------------------------------------зададим свое исключение

class PainError (Exception):
	pass

raise PainError ('information about exception')