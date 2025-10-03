'''
Упражнение №6: Сложный калькулятор
В файле input.txt на первой строке перечислены числа (через пробел),
на второй строке написан символ арифметической операции (+, -, *), 
которую необходимо выполнить с ними,
в третьей строке написано основание системы счисления, 
в которой записаны эти числа. Необходимо вывести в файл 
output.txt результат выполнения арифметической операции 
в той же системе счисления.
'''

def to_ten(value, system): # перевод в десятичную систему
	sys_10_numb = 0
	value = str(value)[::-1]
	
	for i in range(len(value)):
		sys_10_numb += int(value[i]) * (system**i)
	
	return sys_10_numb

def to_nec(value, system):# перевод в другую систему
	res = ""
	
	while value >= system:
		res += str(value % system)
		value = (value - (value % system)) // system
		print(res, value)
		
	res += str(value)
	
	return res[::-1]

with open("input.txt", "r") as f:
	inp = f.readlines()

inp = [i.replace("\n", "") for i in inp if i.replace("\n", "") != ""] #удаление лишних строк и символов перехода
numbers, action, syst = inp[0].split(" "), inp[1], int(inp[2]) #разделение символов и чисел на элементы массива
numbers = [str(to_ten(int(i), syst)) for i in numbers] # переводим все числа в десятичную систему

executing_line = numbers[0]
for i in range(len(numbers)-1): #соединяем поочерёёдно число и знак
	executing_line += action + numbers[i+1]

result = eval(executing_line)

result = to_nec(result, syst) #ответ в указанной системе

with open("output.txt", "w+") as f:
	f.write(str(result))
