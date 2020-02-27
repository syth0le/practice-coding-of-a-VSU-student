.text

.globl main
main:
	li $v0, 5
	syscall
	
	la $t0, ($v0)
	
	li $v0, 5
	syscall
	
	la $t1, ($v0)
	
	addu $t2, $t0, $t1
	mult $t0, $t1
	mflo $t3
	subu $t4, $t0, $t1
	divu $t0, $t1
	mflo $t5
	
	li $v0, 1
	
	la $a0, ($t2)
	syscall
	
	la $a0, ($t3)
	syscall
	
	la $a0, ($t4)
	syscall
	
	la $a0, ($t5)
	syscall
	
	li $v0, 10
	syscall
	
.end main