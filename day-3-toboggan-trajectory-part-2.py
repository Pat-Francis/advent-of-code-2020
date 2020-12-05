# --- Part Two ---
# Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.
# Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

#     Right 1, down 1.
#     Right 3, down 1. (This is the slope you already checked.)
#     Right 5, down 1.
#     Right 7, down 1.
#     Right 1, down 2.
# In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.
# What do you get if you multiply together the number of trees encountered on each of the listed slopes?

terrain = [l.strip() for l in open('day-3-input.txt','r')]
slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
totalTrees = []
trees = 0
x = 0

for slope in slopes:
    for line in terrain[::slope[1]]:

        if line[x] == '#':
            trees += 1
        x += slope[0]
        if x > 30:
            x = x % 31
    totalTrees.append(trees)
    trees = 0
    x = 0

print(totalTrees)
total = 1
for tote in totalTrees:
    total *= tote
print(total)