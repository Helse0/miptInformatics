import matplotlib.pyplot as mpl

with open("sem_4/lab_data.txt", "r", encoding="utf-8") as f:
    data = [int(i.replace("\n", "")) for i in f.readlines() if not "#" in i]

average = [sum(data[:i])/i for i in range(1, len(data))]

mpl.plot([i for i in range(len(average))], average)
mpl.title("Среднее количество зарегстрированных частиц от количества измерений")

mpl.xlabel("измерение")
mpl.ylabel("в среднем зарегистрировано за секунду")

mpl.show()