'''
Упражнение 4. Перестановка
Переставьте соседние элементы в списке. Задача решается в три строки.
'''

a = input().split(" ")
dev_2 = [[a[i] if i % 2 == 0 else None for i in range(len(a))], [a[i] if i % 2 == 1 else None for i in range(len(a))]]
print([[str(dev_2[1][i])+str(dev_2[0][i]) for i in range(len(dev_2[0]))]])
