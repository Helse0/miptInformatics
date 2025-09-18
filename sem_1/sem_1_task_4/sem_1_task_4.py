#Упражнение №4: Калькулятор в файл
#В файле input.txt на первой строке перечислены числа (через пробел), 
#на второй строке написан символ арифметической операции (+, -, *), 
#которую необходимо выполнить с ними. Необходимо вывести в файл 
#output.txt результат выполнения арифметической операции.

with open("input.txt", "r") as f:
	inp = f.readlines()

inp = [i.replace("\n", "") for i in inp if i.replace("\n", "") != ""] #удаление лишних строк и символов перехода
numb, act = inp[0].split(" "), inp[1] #разделение символов и чисел на элементы массива

executing_line = numb[0]
for i in range(len(numb)-1): #соединяем поочерёёдно число и знак
	executing_line +=  act + numb[i+1]
	
print(executing_line)

result = eval(executing_line) #выполняем строку

with open("output.txt", "w+") as f:
	f.write(str(result))
