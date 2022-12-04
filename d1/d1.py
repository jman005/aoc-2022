inventories = []
with open("input.txt", "r") as f:
	cinv = []
	for line in f.readlines():
		if line == "\n":
			inventories.append(cinv)
			cinv = []
		else:
			cinv.append(int(line))
	inventories.append(cinv)


cmax = 0
for inv in inventories:
	isum = sum(inv)
	if isum > cmax:
		cmax = isum
print(cmax)
