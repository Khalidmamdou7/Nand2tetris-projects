# Assembler program that translates assembly programs to binary machine language 
import sys

from helpers import comptrans, desttrans, jumptrans

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

		# Loop over each line
		for x in line:
			# skip lines with comments or white space
			if x.startswith('//') or not x: 
				continue
			# if the line is a a-instruction 
			if x.startswith('@'):
				ainst = x.strip('@')
				binary = bin(int(ainst)).lstrip('0b')
				fw.write('0' * (16 - len(binary)) + f'{binary}\n')

			# if the line is a label
			elif x.startswith('('):
				print('label')
			# if line is C-instruction
			else:
				dest = comp = jump = None

				# if dest exists
				if '=' in x :
					cinst = x.split('=')
					dest = cinst[0]
					# if jump exists
					if ';' in x:
						comp = cinst[1].split(';')[0]	
						jump = cinst[1].split(';')[1]
					else:
						comp = cinst[1]
				elif not '=' in x:
					cinst = x.split(';')
					comp = cinst[0]
					jump = cinst[1]


				# translation
				comp = comptrans(comp)
				dest = desttrans(dest)
				jump = jumptrans(jump)

				fw.write('111' + f'{comp}{dest}{jump}\n')


				




		fr.close()
		fw.close()


if __name__== "__main__":
	main()