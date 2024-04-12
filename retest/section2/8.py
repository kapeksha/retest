# #8.
# a function to read lines from text FileExistsErrorex. test.txt file
# line1
# line2
# .
# .
# .
# .
# input:read_file(test.txt,2)
# output:
# line6
# line7

#Question-8: read last n ines of a file:

file_name=input("Enter filename: ")
n=int(input("Enter no. of last n lines you want to read: "))
with open(file_name,'r') as f:
    lines1=f.readlines()
    last_n_lines=lines1[-n:]
 
for line in last_n_lines:   
    print(line,end='')