// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// pseudo code :
//	if KBD != 0:
//		for (i=0; i< 8193; i++) {
//			RAM[addr] = -1
//  	}
//	else:
//		whiten all the screen 



@8193
M=A			// screen limit =  (256 * 32) + 1 = 8193
	

(LISTEN)
@i
M=1			// i = 0
@SCREEN
D=A
@addr
M=D			// addr = 16384 	(screen's base address)
@KBD
D=M
@WHITE
D;JEQ
@BLACK
D;JNE

(BLACK)
@i
D=M
@8193
D=D-M
@LISTEN
D;JGE		// if i = scrlimit jump to LISTEN

@addr
A=M
M=-1		// RAM[addr] = 111111111111111

@i
M=M+1		// i++
@addr
M=M+1		// addr + i
@BLACK
0;JMP


(WHITE)
@i
D=M
@8193
D=D-M
@LISTEN
D;JGE		// if i = scrlimit jump to LISTEN

@addr
A=M
M=0		// RAM[addr] = 0000000000000000

@i
M=M+1		// i++
@addr
M=M+1 		// addr + 1
@WHITE
0;JMP




