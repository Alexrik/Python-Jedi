#def exc (text):
	#assert text != ''
	#print(str(text) + '!')

#exc ('') # если текст пустой, выведет assertionError

#def num (number):
	#assert number > 0, "number should be bigger than zero"
	#print (str(number))

#num (-10)

# --------------------------Open File
#filename = input ('file name: ')
#content = input ('What do you want to write in file? ')
#file = open (filename, 'w')

#file.write (content)

#print ( str(len(file.read())) )

#file.close()

# r - чтение файла
# w - перезапись файла
# a - добавление в файл
# b - Binary mode считывает музыкальные файлы, видео файлы и все прочее.

#file = open ('test.txt', 'r')

#print (file.read (5))# файл может читаться по колличеству байтов
#file.close()

#file = open ('test.txt', 'a')

#file.write ('TEST')

#file.close()

# -----------------небольшая программа для копирования файлов

filename_1 = input('What file you want to backup: ')
filename_2 = 'backup--' + filename_1

file_1 = open(filename_1, 'rb')
file_2 = open(filename_2, 'wb')

file_2.write (file_1.read())

file_1.close
file_2.close

print ('File copied')

file = open ('test.txt', 'r')

strings = file.readlines() # позволяет читать файлы по строкам

for string in strings:
	print (string)

print (strings)

file.close()

with open('test.txt', 'r') as f: # конструкция with позволяет не писать
	print(f.read())				 # каждый раз .close()
