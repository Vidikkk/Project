import random
m = int(input("Введіть кількість слів: "))
n = int(input("Введіть кількість символів у слові: "))

def random_words(m, n):
    abc = 'абвгґдежзийклмнопрстуфхцчшщьюя'
    words = []
    
    for i  in range(m):
        word = ''.join(random.choice(abc) for i in range(n))
        words.append(word)
        
    return ' '.join(words)
result = random_words(m, n )
print(result)