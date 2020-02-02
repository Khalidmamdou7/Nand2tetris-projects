def comptrans(comp):
	if comp == '0':
		comp = '101010'
		acomp = '0'
	elif comp == '1':
		comp = '111111'
		acomp = '0'
	elif comp == '-1':
		comp = '111010'
		acomp = '0'
	elif comp =='D':
		comp = '001100'
		acomp = '0'
	elif comp == 'A':
		acomp = '0'
		comp = '110000'
	elif comp == 'M':
		acomp = '1'
		comp = '110000'
	elif comp == '!D':
		acomp = '0'
		comp = '001101'
	elif comp == '!A':
		acomp = '0'
		comp = '110001'
	elif comp == '!M':
		acomp = '1'
		comp = '110001'
	elif comp == '-D':
		acomp = '0'
		comp = '001111'
	elif comp == '-A':
		acomp = '0'
		comp = '110011'
	elif comp == '-M':
		acomp = '1'
		comp = '110011'
	elif comp == 'D+1':
		acomp = '0'
		comp = '011111'
	elif comp == 'A+1':
		acomp = '0'
		comp = '110111'
	elif comp == 'M+1':
		acomp = '1'
		comp = '110111'
	elif comp == 'D-1':
		acomp = '0'
		comp = '001110'
	elif comp == 'A-1':
		acomp = '0'
		comp = '110010'
	elif comp =='M-1':
		acomp = '1'
		comp = '110010'
	elif comp == 'D+A':
		acomp = '0'
		comp = '000010'
	elif comp == 'D+M':
		acomp = '1'
		comp = '000010'				
	elif comp == 'D-A':
		acomp = '0'
		comp = '010011'
	elif comp == 'D-M':
		acomp = '1'
		comp = '010011'
	elif comp == 'A-D':
		acomp = '0'
		comp = '000111'
	elif comp == 'M-D':
		acomp = '1'
		comp = '000111'
	elif comp == 'D&A':
		acomp = '0'
		comp = '000000'
	elif comp == 'D&M':
		acomp = '1'
		comp = '000000'
	elif comp == 'D|A':
		acomp = '0'
		comp = '010101'
	elif comp == 'D|M':
		acomp = '1'
		comp = '010101'
	else:
		acomp = 'Error'

	comptranslated = acomp + comp
	return comptranslated

def desttrans(dest):

	if dest == None:
		dest = '000'
	elif dest == 'M':
		dest = '001'
	elif dest == 'D':
		dest = '010'
	elif dest == 'MD':
		dest = '011'
	elif dest == 'A':
		dest = '100'
	elif dest == 'AM':
		dest = '101'
	elif dest == 'AD':
		dest = '110'
	elif dest == 'AMD':
		dest = '111'
	else:
		dest = 'Error'

	return dest 

def jumptrans(jump):

	if jump == None:
		jump = '000'
	elif jump == 'JGT':
		jump = '001'
	elif jump == 'JEQ':
		jump = '010'
	elif jump == 'JGE':
		jump = '011'
	elif jump == 'JLT':
		jump = '100'
	elif jump == 'JNE':
		jump = '101'
	elif jump == 'JLE':
		jump = '110'
	elif jump == 'JMP':
		jump = '111'
	else:
		dest = 'Error'

	return jump 

def decimaltobin(decimal):
	"""Convert decimal value into binary 2's complement"""

	binary = bin(int(decimal)).lstrip('0b')
	binary2comp = '0' * (16 - len(binary)) + f'{binary}'

	return binary2comp 



def getsymbol(command):
	value = command.strip(' ()@')
	return value 
