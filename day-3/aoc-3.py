import re
import numpy as np

def list_cleanup(l):
	l = [x.strip().split(',') for x in l]
	
	temp = re.compile('([a-zA-Z]+)([0-9]+)')
	first_wire = [temp.match(x).groups() for x in l[0]]
	second_wire = [temp.match(x).groups() for x in l[1]]
	
	wires = [first_wire, second_wire]
	
	return wires
	
# def create_matrix(first_wire, second_wire):for x in first_wire:
# 		if x[0] == 'U':
# 			fw_ver_ind.append(fw_ver_ind[-1] - int(x[1]))
# 		elif x[0] == 'R':
# 			fw_hor_ind.append(fw_hor_ind[-1] + int(x[1]))
# 		elif x[0] == 'D':
# 			fw_ver_ind.append(fw_ver_ind[-1] + int(x[1]))
# 		elif x[0] == 'L':
# 			fw_hor_ind.append(fw_hor_ind[-1] - int(x[1]))
# 			
# 	for x in second_wire:
# 		if x[0] == 'U':
# 			sw_ver_ind.append(sw_ver_ind[-1] - int(x[1]))
# 		elif x[0] == 'R':
# 			sw_hor_ind.append(sw_hor_ind[-1] + int(x[1]))
# 		elif x[0] == 'D':
# 			sw_ver_ind.append(sw_ver_ind[-1] + int(x[1]))
# 		elif x[0] == 'L':
# 			sw_hor_ind.append(sw_hor_ind[-1] - int(x[1]))
# 	
# 	max_ver_ind = max(fw_ver_ind + sw_ver_ind)
# 	min_ver_ind = min(fw_ver_ind + sw_ver_ind)
# 	max_hor_ind = max(fw_hor_ind + sw_hor_ind)
# 	min_hor_ind = min(fw_hor_ind + sw_hor_ind)
# 	
# 	print max_ver_ind
# 	print min_ver_ind
# 	print max_hor_ind
# 	print min_hor_ind
# 
# 	# mat = [] # np.zeros([max_ver_ind - min_ver_ind + 1, max_hor_ind - min_hor_ind + 1])
# 	origo = [-min_ver_ind, -min_hor_ind]
# 	
# 	mat = np.full((max_ver_ind - min_ver_ind + 1, max_hor_ind - min_hor_ind + 1), cell())
# 	print mat
# 			
# 	# print mat[-min_ver_ind][-min_hor_ind].origin
# 	print mat[0][0].origin
# 	
# 	return mat, origo
	
	

def find_intersection(wires):
	
	coordinates = []
	
	x = 0
	y = 0
	
	print wires
	
	for wire in wires:
		coordinates
		for i in wire:
			if i[0] == 'U':
				print 'U'
			if i[0] == 'R':
				print 'R'
			if i[0] == 'D':
				print 'D'
			if i[0] == 'L':
				print 'L'

	
if __name__=="__main__":
	f = open('input-3.txt', 'r')
	
	l = f.readlines()
	l_test = ['R8,U5,L5,D6\n', 'U7,R6,D4,L4\n']
	l_test2 = ['R75,D30,R83,U83,L12,D49,R71,U7,L72\n', 'U62,R66,U55,R34,D71,R55,D58,R83\n']
	wires = list_cleanup(l_test)
	print wires[0]
	print wires[1]
		
	print find_intersection(wires)


	# l = [line.split(',') for line in l

	