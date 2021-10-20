
def diagnostic_program(input, program):
	
	prgm = program[:]
	p = 0
	output = 0
	
	while p < len(prgm):
		
		# print p
		
		abcde = prgm[p].zfill(5)
		a = abcde[0] # param 3
		b = abcde[1] # param 2
		c = abcde[2] # param 1
		opcode = abcde[3:]
		
		if opcode == '01':
			param_one = prgm[int(prgm[p + 1])] if c == '0' else prgm[p + 1]
			param_two = prgm[int(prgm[p + 2])] if b == '0' else prgm[p + 2]
			param_three = prgm[p + 3]
			print("Addition " + str(param_one) + " with " + str(param_two) + " to address " + str(param_three))
			prgm[int(param_three)] = str(int(param_one) + int(param_two))
			p += 4
			
		if opcode == '02':
			param_one = prgm[int(prgm[p + 1])] if c == '0' else prgm[p + 1]
			param_two = prgm[int(prgm[p + 2])] if b == '0' else prgm[p + 2]
			param_three = prgm[p + 3]
			print("Multiplication " + str(param_one) + " with " + str(param_two) + " to address " + str(param_three))
			prgm[int(param_three)] = str(int(param_one) * int(param_two))
			p += 4
		
		if opcode == '03':
			print("Opcode 3 takes a single integer as input")
			param_one = prgm[p + 1]
			print("Inputs " + str(input) + " to address " + str(param_one))
			prgm[int(param_one)] = str(input)
			p += 2
		
		if opcode == '04':
			print("Opcode 4 outputs the value of its only parameter")
			param_one = prgm[p + 1]
			output = prgm[int(param_one)]
			print("Outputs : " + str(prgm[int(param_one)]) + " from address " + str(param_one))
			p += 2
			
		if opcode == '05':
			print("Opcode 5 is jump-if-true")
			param_one = prgm[int(prgm[p + 1])] if c == '0' else prgm[p + 1]
			param_two = prgm[p + 2]
			print("Pointer jumps to " + str(param_two))
			p = int(param_two) if param_one != '0' else p + 2
		
		if opcode == '06':
			print("Opcode 6 is jump-if-false")
			param_one = prgm[int(prgm[p + 1])] if c == '0' else prgm[p + 1]
			param_two = prgm[p + 2]
			print("Pointer jumps to " + str(param_two))
			print param_one
			print p
			p = int(param_two) if param_one == '0' else p + 2
			print p
			
		if opcode == '07':
			print("Opcode 7 is less than")
			param_one = prgm[int(prgm[p + 1])] if c == '0' else prgm[p + 1]
			param_two = prgm[int(prgm[p + 2])] if b == '0' else prgm[p + 2]
			param_three = prgm[p + 3]
			# print("Multiplication " + str(param_one) + " with " + str(param_two) + " to address " + str(param_three))
			prgm[int(param_three)] = 1 if int(param_one) < int(param_two) else 0
			p += 4
			
		if opcode == '08':
			print("Opcode 8 is equals")
			param_one = prgm[int(prgm[p + 1])] if c == '0' else prgm[p + 1]
			param_two = prgm[int(prgm[p + 2])] if b == '0' else prgm[p + 2]
			param_three = prgm[p + 3]
			# print("Multiplication " + str(param_one) + " with " + str(param_two) + " to address " + str(param_three))
			prgm[int(param_three)] = 1 if int(param_one) == int(param_two) else 0
			p += 4
			
		if opcode == '99':
			return output

	
	return output
	

if __name__=="__main__":
	f = open('input-5.txt', 'r')
	
	program = f.readlines()
	program = [x.strip().split(',') for x in program][0]
	
	# print program
	
	test_program = ['1002','4','3','4','33']
	test_program2 = ['3','0','4','0','99']
	
	test_program3 = ['3','21','1008','21','8','20','1005','20','22','107','8','21','20','1006','20','31','1106','0','36','98','0','0','1002','21','125','20','4','20','1105','1','46','104','999','1105','1','46','1101','1000','1','20','4','20','1105','1','46','98','99']
	
	test_program_position_jump = ['3','12','6','12','15','1','13','14','13','4','13','99','-1','0','1','9']
	test_program_immediate_jump = ['3','3','1105','-1','9','1101','0','0','12','4','12','99','1']

	
	input = 8
	
	print("Answer to Part One: " + str(diagnostic_program(input, program)))