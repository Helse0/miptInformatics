numbers = input().split()

max_count = 0
most_frequent = None

for i in range(len(numbers)):
    current_num = numbers[i]
    count = 0
    
    for j in range(len(numbers)):
        if numbers[j] == current_num:
            count += 1
    
    if count > max_count:
        max_count = count
        most_frequent = current_num

print(most_frequent)