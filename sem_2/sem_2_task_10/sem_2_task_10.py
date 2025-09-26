with open("sem_2/sem_2_task_10/input.txt", "r", encoding="utf-8") as f:
    data = f.read()

words = data.split(" ")
vowels = ["о", "е", "и", "а", "э", "у", "ы", "я", "ю", "ё"]
consonants = [
    'б', 'в', 'г', 'д', 'ж', 
    'з', 'й', 'к', 'л', 'м', 
    'н', 'п', 'р', 'с', 'т', 
    'ф', 'х', 'ц', 'ч', 'ш', 
    'щ', 'ъ', 'ь'
]

res_words = []

for iter, i in enumerate(words):
    word = list(i.lower())
        
    for iter, j in enumerate(word):
        if (j in vowels) and (iter != len(word)-1) and (word[iter+1] in consonants):
            word[iter] = j + "с" + j
    
    res_words.append("".join(word))
    
print(" ".join(res_words))