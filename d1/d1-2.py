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


cmaxes = [0,0,0]
for inv in inventories:
	isum = sum(inv)
	for i in range(0, len(cmaxes)):
		if isum > cmaxes[i]:
			cmaxes.insert(i, isum)
			cmaxes = cmaxes[0:3]
			break
print(cmaxes)
print(sum(cmaxes))
