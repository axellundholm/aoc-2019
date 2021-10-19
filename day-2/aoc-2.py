def run(l, noun, verb):
	
	
	list = l[:]
	list[1] = noun
	list[2] = verb
	
	for i in range(len(list)/4):
		
		opcode = list[i * 4]
		parameter_one = list[i * 4 + 1]
		parameter_two = list[i * 4 + 2]
		parameter_three = list[i * 4 + 3] 

		
		if opcode == 1:
			list[parameter_three] = list[parameter_one] + list[parameter_two]
			
		elif opcode == 2:
			list[parameter_three] = list[parameter_one] * list[parameter_two]
			
		elif opcode == 99: 
			return list[0] 
			
		else:
			print("ERROR")
			
def find_noun_verb(list, output):
	
	
	
	for i in range(100):
		for j in range(100):
			if run(l, i, j) == output:
				return 100 * i + j

	
	


if __name__=="__main__":
	f = open('input-2.txt', 'r')
	
	# l = f.readlines()
	# l = [int(x.strip()) for x in l]

	l = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,19,6,23,2,23,13,27,1,27,5,31,2,31,10,35,1,9,35,39,1,39,9,43,2,9,43,47,1,5,47,51,2,13,51,55,1,55,9,59,2,6,59,63,1,63,5,67,1,10,67,71,1,71,10,75,2,75,13,79,2,79,13,83,1,5,83,87,1,87,6,91,2,91,13,95,1,5,95,99,1,99,2,103,1,103,6,0,99,2,14,0,0]
	
	l_test = [1,9,10,3,2,3,11,0,99,30,40,50]
	output = 19690720

	print("Answer to Part One: " + str(run(l, 12, 2)))

	print("Answer to Part Two: " + str(find_noun_verb(l, output)))