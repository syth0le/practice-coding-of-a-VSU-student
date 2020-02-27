.data
readyStr: .asciiz "python"
EntStr: .asciiz "VseVotEtiVashiJazikiGovnoSobacheePythonRulit"
True: .asciiz "True"
False: .asciiz "False"

.text
.globl main
main:
li $v0,8
la $a0, EntStr
syscall
la $t0, readyStr # first string counting
la $t2, EntStr # string from console counting
loop:
lb $t1, ($a0) # load next one character to t1
lb $t3, ($t0)
addi $a0, $a0, 1 
addi $t0, $t0, 1 
beqz $t3, exit # if $t3 == 0 go to modul exit
beq $t1, $t3, loop
li $v0, 4
la $a0, False
syscall
li $v0,10
syscall
exit:
li $v0, 4
la $a0, True
syscall
li $v0,10
syscall
.end main
