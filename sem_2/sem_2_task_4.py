''' Упражнение 4. Перестановка
Переставьте соседние элементы в списке. Задача решается в три строки.
'''

''' Длинная версия:
i = input().split()
new = []
for j in range(len(i) - (len(i) % 2)):
	if j % 2 == 0:
		new.append(i[j+1])
	else:
		new.append(i[j-1])
		
print(" ".join(new if len(i) % 2 == 0 else new + [i[len(i) - 1]]))
'''

i = input().split()
new = [i[j+1] if j % 2 == 0 else i[j-1] for j in range(len(i) - (len(i) % 2))]
print(" ".join(new if len(i) % 2 == 0 else new + [i[len(i) - 1]]))
