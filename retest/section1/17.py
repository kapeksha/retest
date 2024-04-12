
#17.

my_string=" I will score at least 60"
k=[]
for i in my_string.lower():
    if i not in 'aeiou':
        k.append(i)
print(k)

Ans: [' ', ' ', 'w', 'l', 'l', ' ', 's', 'c', 'r', ' ', 't', ' ', 'l', 's', 't', ' ', '6', '0']
