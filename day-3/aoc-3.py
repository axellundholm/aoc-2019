import re

def list_cleanup(l):
	
	l = [x.strip().split(',') for x in l]
	
	temp = re.compile('([a-zA-Z]+)([0-9]+)')
	first_wire = [temp.match(x).groups() for x in l[0]]
	second_wire = [temp.match(x).groups() for x in l[1]]
	
	wires = [first_wire, second_wire]
	
	return wires
	
def find_intersection(wires):
	
	coordinates = []
	w = 0
	
	for wire in wires:
		x = 0
		y = 0
		coordinates.append([[x, y]])
		for i in range(len(wire)):
			if wire[i][0] == 'U':
				for step in range(int(wire[i][1])):
					y += 1
					coordinates[w].append([x, y])
			elif wire[i][0] == 'R':
				for step in range(int(wire[i][1])):
					x += 1
					coordinates[w].append([x, y])
			elif wire[i][0] == 'D':
				for step in range(int(wire[i][1])):
					y -= 1
					coordinates[w].append([x, y])
			elif wire[i][0] == 'L':
				for step in range(int(wire[i][1])):
					x -= 1
					coordinates[w].append([x, y])
		
		w += 1
	
	# print coordinates[0]
	# print(tuple(row) for row in coordinates[0])
	print(set(tuple(row) for row in coordinates[0]))
	
	intersections = set(tuple(row) for row in coordinates[0]).intersection(set(tuple(row) for row in coordinates[1]))	
	
	distance = []
	
	for ins in intersections:
		distance.append(abs(ins[0]) + abs(ins[1]))
		
	return sorted(set(distance))[1]
	
if __name__=="__main__":
	f = open('input-3.txt', 'r')
	
	l = f.readlines()
	l_test = ['R8,U5,L5,D3\n', 'U7,R6,D4,L4\n']
	l_test2 = ['R75,D30,R83,U83,L12,D49,R71,U7,L72\n', 'U62,R66,U55,R34,D71,R55,D58,R83\n']
	wires = list_cleanup(l)
	
	
	print("Answer to Part One: " + str(find_intersection(wires)))
