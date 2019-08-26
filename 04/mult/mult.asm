// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// pseudo code
// i = 0
// a = R0 , b = R1 , c = R2
//	 	if b > i :
// 				c = c + a;
//				i++ ;
// 		else:
// 				end

@R0
D=M
@a
M=D 	// a = R0
@R1
D=M
@b
M=D 	// b = R1
@c
M=0		// c = 0
@i
M=0		// i = 0
@R2
M = 0   // we want to clear the result reg for answer


(LOOP)
@i
D=M
@b
D=D-M
@STOP
D;JGE	// if i >= b jump to STOP
@c
D=M
@a
D=D+M
@c
M=D 	// c = c + a
@i
M=M+1	// i++
@LOOP
0;JMP

(STOP)
@c
D=M
@R2
M=D 	// RAM[2] = c

(END)
@END
0;JMP
