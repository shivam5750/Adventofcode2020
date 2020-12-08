map = []
with open('dAY3input.txt')as input:
	for line in input:
		road =line.rstrip()
		map.append(road)
size =len(road)

def count_trees(arr, str_len, right, down):
	j = right
	trees = 0
	for i in range(len(map)):
		if j >= len(road):
			j = j -31

		if i >= len(map)-down:
			break

		if  map[i+ down][j] == '#':
			trees +=1
		j +=right
	return trees

print(count_trees(map,size, 3, 1 ))

# part 2

print(count_trees(map,size, 1, 1 ))
print(count_trees(map,size, 3, 1 ))
print(count_trees(map,size, 5, 1 ))
print(count_trees(map,size, 7, 1 ))
print(count_trees(map,size, 1, 2 ))




