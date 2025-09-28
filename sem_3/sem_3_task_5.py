'''
Упражнение 5
Создайте матрицу размером NxM, заполненную "спиралью".
Умножьте каждую строку получившейся матрицы на номер строки, выведите результат.
'''
def fill(n, m):
    matrix = [[0] * m for _ in range(n)]

    top, bottom = 0, n - 1
    left, right = 0, m - 1
    
    num = 1

    while top <= bottom and left <= right:
        # вправо
        for col in range(left, right + 1):
            matrix[top][col] = num
            num += 1
        top += 1

        # вниз
        for row in range(top, bottom + 1):
            matrix[row][right] = num
            num += 1
        right -= 1

        # влево
        if top <= bottom:
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1

        # вверх
        if left <= right:
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = num
                num += 1
            left += 1

    return matrix


def rows(matrix):
    result = []
    for i, row in enumerate(matrix):
        m_row = [x * (i + 1) for x in row]
        result.append(m_row)
    
    return result


n = int(input())
m = int(input())

spiral = fill(n, m)
result = rows(spiral)

from pprint import pprint
#pprint(spiral)
pprint(result) # Не уверен, что понял задание правильно, но, кажется, надо так.