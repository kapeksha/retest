
#12.filter even odd no. from list of integer using lambda function

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, num))
odd_numbers = list(filter(lambda x: x % 2 != 0, num))

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)