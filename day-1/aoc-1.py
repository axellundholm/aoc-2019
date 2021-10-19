import math

def loop_list(list, rec):
	
	sum = 0
	
	for i in list:
		sum += calc_fuel(i, rec)
		
	return sum

def calc_fuel(mass, rec):
	
	fuel = int(math.floor(mass / 3)) - 2
	
	if fuel > 0 and rec:
		fuel += calc_fuel(fuel, rec)
	
	return max(fuel, 0)



if __name__=="__main__":
	f = open('input-1.txt', 'r')
	
	l = f.readlines()
	l = [int(x.strip()) for x in l]

	
	print("Answer to Part One: " + str(loop_list(l, rec = False)))
	print("Answer to Part Two: " + str(loop_list(l, rec = True)))