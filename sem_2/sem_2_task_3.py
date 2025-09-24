def mirrored(s): #ничего не проверяет, просто возвращает отражённую
    mirror_dict = { #исходники и отражённые
        'A': 'A', 'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O', 'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', '1': '1', '8': '8',
        'E': '3', 'J': 'L', 'S': '2', 'Z': '5',
        '3': 'E', 'L': 'J', '2': 'S', '5': 'Z'
    }
    
    mirrored_chars = []
    
    for char in s:
        if char in mirror_dict:
            mirrored_chars.append(mirror_dict[char])
        else:
            return
    
    mirrored_str = ''.join(mirrored_chars)
    
    return mirrored_str

def check(s):
    palindrome = (s == s[::-1])
    mirror =  (mirrored(s) == s[::-1])
    
    print(type(palindrome), type(mirror))
    if palindrome and mirror:
        return f"{s} is a mirrored palindrome."
    elif palindrome:
        return f"{s} is a regular palindrome."
    elif mirror:
        return f"{s} is a mirrored string."
    else:
        return f"{s} is not a palindrome."

print(check(input()))
