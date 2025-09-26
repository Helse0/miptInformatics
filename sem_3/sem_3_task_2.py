def prime(a, res=[]):    
    if a != 1:
        for i in range(2, int(a**0.5)+1):
            if a % i == 0:
                return prime(a//i, res+[i])
        
        return prime(1, res+[a])
    
    else:
        return a, res+[1]

print(sorted(prime(int(input()))[1])) # выводит массив,содержащий все простые делители по возрастанию