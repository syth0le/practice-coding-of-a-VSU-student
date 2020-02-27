.data
EntStr: .asciiz "ssilkaStalina"
len: .word 5  # dont forgive to load my num to this var

.text

.globl main

main:	
	li $v0, 8
	la $a0, EntStr
	syscall
	li $t2, 0
	li $t3, 0
	loop:
		lb $t1,($a0)
		addi $a0, $a0, 1
		addi $t2, $t2, 1
		bne $t1, $t3, loop
		beq $t1, $t3, exit
	exit:
		li $v0, 1
		subu $t2, 2
		la $a0, ($t2)
		syscall
.end main






	