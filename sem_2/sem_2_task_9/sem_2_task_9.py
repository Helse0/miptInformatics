with open("sem_2/sem_2_task_9/input.txt", "r") as f:
    data = f.read()
    print(sum([data.count(i) for i in ".!?"]))