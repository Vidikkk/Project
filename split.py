s = (input("Введіть  укр. слів:"))
s1 = s.split()
s2 = [len(word) for word in s1 ]
max = max(s2)
min = min(s2)
print ("найбільша кількість символів:", min)
print ("найменша кількість символів:", max)
