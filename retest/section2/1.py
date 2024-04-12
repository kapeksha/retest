#1.give list in python and provided positions of elements write program to swipe two elements in list

list1=[int(x) for x in input("Enter elements of list in space separated format: ").split(' ')]
pos1=int(input("Enter position1: "))
pos2=int(input("Enter position2: "))

x=list1[pos1]
list1[pos1]=list1[pos2]
list1[pos2]=x

print(list1)