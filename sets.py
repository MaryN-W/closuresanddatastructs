# Set => Unodered - Not indexed - mutable - no duplicates
# List - ordered(indexed) collection of items - mutable - can have duplicates

names_set = {'Kamau', 'Ndungu', 'Kiarie', 'Otieno'}

# print(names_set[1]) # Set cannot access index
names_set.add('Wangari') # accessing the set to add items
names_set.remove('Kamau')
print(names_set)

set1 = {1, 2, 3, 4, 5}
set2 = {1, 3, 5, 7, 9}

print(set1.union(set2)) # result => duplicates removed
print(set1.intersection(set2))  # Result => common elements => useful in data processing
print(set1.difference(set2)) # Output => 2, 4 / items in set1 but not in set2 
# print(set1 - set2) same operation as above, but using method above is more readable
