
#7. total no of digits

input_number = 75869456
total_digits = 0
while input_number != 0:
    total_digits += 1
    input_number //= 10

print("Total number of digits:", total_digits)