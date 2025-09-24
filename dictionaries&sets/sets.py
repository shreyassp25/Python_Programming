# collection of non-repetitive elements
# 1. Sets are unordered => Element’s order doesn’t matter
# 2. Sets are unindexed => Cannot access elements by index
# 3. There is no way to change items in sets.
# 4. Sets cannot contain duplicate values.

s=set()

s.add(1)
s.add(2)

print(s)


""" Consider the following set:
s = {1,8,2,3}
• len(s): Returns 4, the length of the set
• s.remove(8): Updates the set s and removes 8 from s.
• s.pop(): Removes an arbitrary element from the set and return the element
    removed.
• s.clear():empties the set s.
• s.union({8,11}): Returns a new set with all items from both sets. {1,8,2,3,11}.
• s.intersection({8,11}): Return a set which contains only item in both sets {8}.   """