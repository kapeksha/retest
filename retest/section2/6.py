
#6.
# concider 2sets:
# find intersection of sets
# find union of sets
# find maximum value from union of sets
# find minimum value from union of sets
# find length of from union of sets


set1={1,2,3,4}
set2={4,5,6,7}
print("intersection is:",set1.intersection(set2))
print("union is:",set1.union(set2))
print("max is:",max((set1.union(set2))))
print("min is:",min((set1.union(set2))))
print("length is:",len(set1.union(set2)))