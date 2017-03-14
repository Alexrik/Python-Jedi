bool_1 = True
bool_2 = False

#print (bool_1)

#print (10 == 11)

#---------------лексиграфическое сравнение

# у каждой буквы есть свой вес

#print ('str' > 'sta')

weather = 'snow'
time = 'day'

#if weather == 'snow':
	#print ('you are crazy!')
	#if time == 'night':
	#	print ('and it\'s night')
	#if time == 'day':
	#	print ('cold!')
	
#if weather == 'rain':
	#print ('it\'s rain')

#if time == 'night':
	#print('not right now')
#elif time == 'morning':
	#print('breakfast ?')
#else:
	#print('right now!')

#----------------------реализация множественных условий

if weather == 'snow' and time == 'night':
	print ('NO!')

if weather == 'snow' or time == 'night':
 	print ('yes')

if not weather == 'snow':
	print('something')



