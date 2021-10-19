
def check_pwd(pwd, part):
	
	pwd_int = False
	pwd_len = False
	pwd_adj = False
	pwd_geq = True
	
	if isinstance(pwd, int): pwd_int = True
	
	if len(str(pwd)) == 6: pwd_len = True
	
	for char_ind in range(len(str(pwd)) - 1):
		if int(str(pwd)[char_ind]) > int(str(pwd)[char_ind + 1]): pwd_geq = False

	
	if part == 1:
		for i in range(10):
			if str(pwd).count(str(i)) >= 2: pwd_adj = True
	
	elif part == 2:
		for i in range(10):
			if str(pwd).count(str(i)) == 2: pwd_adj = True
	
	else: return False
	
	return pwd_int and pwd_len  and pwd_geq and pwd_adj
	

if __name__=="__main__":
	
	range_start = 372304
	range_stop = 847060
	
	nbr_of_passwords = [0,0]
	
	for pwd in range(range_start, range_stop):
		if check_pwd(pwd, 1): 
			nbr_of_passwords[0] += 1
			if check_pwd(pwd, 2): nbr_of_passwords[1] += 1 
		
	
	print("Answer to Part One: " + str(nbr_of_passwords[0]))
	print("Answer to Part Two: " + str(nbr_of_passwords[1]))
	
	