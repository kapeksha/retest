#4. sort dictionaries by ascending order by key

my_dict = {'ravi':10,'rajnish':9,'sanjeev':15,'yash':2,'suraj':32}
sorted_dict = dict(sorted(my_dict.items()))
print(sorted_dict)
# order by value
my_dict = {'ravi':10,'rajnish':9,'sanjeev':15,'yash':2,'suraj':32}
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(sorted_dict)
