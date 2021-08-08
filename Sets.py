# Sets

# part 1
listA = {"Pocket Knife","Sleeping Bag","Water Bottle","Fire Starter","First Aid Kit"}
listB = {"Fire Starter","First Aid Kit","Pocket Knife","Compass","Head Lamp"}

# part 2
print("***Part 2***")
# display items in list A
print("List A:")
for item in listA:
    print(item)
print("Iteration Ended.\n")

# display items in listB
print("List B:")
for item in listB:
    print(item)
print("Iteration Ended.\n")

# part 3
print("***Part 3***")
# display the full list of camping items
print("Full items:")
for item in listA.union(listB):
    print(item)
print("Iteration Ended.\n")

# part 4
print("***Part 4***")
# display the list of items common to each camper
print("Common items:")
for item in listA.intersection(listB):
    print(item)
print("Iteration Ended.\n")

# part 5
print("***Part 5***")
# display the list of items that each camper
# is bringing that does not include those that are common between them.
print("Items that are not common:")
for item in listA.symmetric_difference(listB):
    print(item)  
print("Iteration Ended.")

