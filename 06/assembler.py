# Assembler program that translates assembly programs to binary machine language 
import sys

from helpers import comptrans, desttrans, jumptrans,decimaltobin,getsymbol

def main():
	if len(sys.argv) != 2:
		print("Invalid format! Correct one: 'Assembler filename.asm' ")
	else:
		# Opening files to read from and to write into
		argv_1 = sys.argv[1]
		fasm = argv_1.split('.')
		fname = fasm[0]
		fr = open(f"{argv_1}", 'r')
		fw = open("{0}.hack".format(fname), "w+")

		# Split each line in the file
		lines = fr.read()
		line = lines.splitlines()
		lineslen = len(line)

		# Construct symbol table 
		# Pre-defined symbols
		symbol ={}
		symbol = {'SP': 0, 'LCL': 1, 'ARG': 2,'THIS' : 3, 'THAT': 4, 'R0': 0, 'R1': 1,'R2':2,'R3':3,'R4':4,'R5':5,'R6':6,'R7':7,'R8':8,'R9':9,'R10':10,'R11':11,'R12':12,'R13':13,'R14':14,'R15':15,'SCREEN':16384,'KBD':24576}
		symc = 16
		linec = 0

		# First pass
		for x in line:
			if not x:
				continue
			elif x.startswith('('):
				label = getsymbol(x)
				value = symbol.get(label)
				if value == None:
					symbol[label] = linec
			elif not x.startswith('//' or '('):
				linec+=1


		
		# Second pass
		# Loop over each line
		for x in line:
			# skip lines with labels, comments or white space
			if x.startswith('//') or x.startswith('(') or not x: 
				continue
			# if the line is a a-instruction 
			elif '@' in x:
				ainst = getsymbol(x)
				# if it's not a symbol
				if ainst.isdecimal():
					binary = decimaltobin(ainst)
				else:
					# Check if it exists in symbol table
					value = symbol.get(ainst)
					# Update symbol table
					if value == None:
						symbol[ainst] = symc
						symc += 1
						value = symbol.get(ainst)
						binary = decimaltobin(value)
					else:
						binary = decimaltobin(value)

				fw.write(f'{binary}\n')

			# if line is C-instruction
			else:
				dest = comp = jump = None

				if '//' in x:
					inst = x.split('//')[0]
					inst = inst.strip(' ')
				else:
					inst=x.strip(' ')

				# if dest exists
				if '=' in inst :
					cinst = inst.split('=')
					dest = cinst[0]
					# if jump exists
					if ';' in inst:
						comp = cinst[1].split(';')[0]	
						jump = cinst[1].split(';')[1]
					else:
						comp = cinst[1]
				elif not '=' in inst:
					if ';' in inst:
						cinst = inst.split(';')
						comp = cinst[0]
						jump = cinst[1]
					else:
						comp = inst


				# translation
				comp = comptrans(comp)
				dest = desttrans(dest)
				jump = jumptrans(jump)

				fw.write('111' + f'{comp}{dest}{jump}\n')


				
		fr.close()
		fw.close()


if __name__== "__main__":
	main()