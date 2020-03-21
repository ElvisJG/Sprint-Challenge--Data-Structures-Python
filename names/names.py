import time
from BST import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# list to hold filtered names
filteredNames = []
# Initialize binary search tree, if there is no value given it will fail
searchTree = BinarySearchTree("")
# iterate through the first list and add all of the names
for name in names_1:
    searchTree.insert(name)
# iterate through the second list
for name in names_2:
    # use the binary search tree function contains to check names from the second list
    if searchTree.contains(name):
        # add duplicate names to the filteredNames array
        filteredNames.append(name)


end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
