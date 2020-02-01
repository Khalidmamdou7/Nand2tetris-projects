# Assembler program that translates assembly programs to binary machine language 
from sys 


def main():
	if len(sys.argv) != 2:
		print("Invalid format! Correct one: 'Assembler filename.asm' ")
	else
		# Opening files to read from and to write into
		argv_1 = sys.argv[1]
		fasm = argv_1.split('.')
		fname = fasm[0]
		fr = open(f"{argv_1}", 'r')
		fw = open("{0}.hack".format(fname), "w+")

		# Split each line in the file
		lines = fr.read()
		line = lines.splitlines()

		





		fr.close()
		fw.close()


if __name__== "__main__":
	main()