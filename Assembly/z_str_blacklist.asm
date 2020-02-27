.data
string:	.asciiz  "I like vichtech"
EntStr: .asciiz  "000000000000000000000000000000"
True: .asciiz "True"
False: .asciiz "False"
.text
.globl main
.ent main
main:
	li $v0, 8
	la $a0, EntStr
	syscall
	jal lenString
	sub $t0, $t0, 1
	move $a0, $t0
	li $v0, 1
	syscall
	li $v0, 10
	syscall
	
lenString:
	la $t0, string
	la $t2, EntStr
	loop:
	lb $t1, ($a0)
	lb $t3, ($t0)
	addi $a0, $a0, 1
	addi $t0, $t0, 1
	beqz $t3, exit
	beq $t1, $t3, loop
	li $v0, 4
	la $a0, False
	syscall
exit:
	li $v0, 4
	la $a0,True
	syscall
jr $ra