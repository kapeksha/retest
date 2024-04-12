#3.create list of tuples having 1st element as no. and 2nd no. as cube of no

numbers = [2, 3, 5, 7, 10]  
list_of_tuples = [(num, num ** 3) for num in numbers]
print(list_of_tuples)