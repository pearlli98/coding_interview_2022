"""
Push 5
Push "I am "
Add
Print_and_pop
Push "Jumping"
Print_and_pop
Jump 0

[5, 10, 15, ]

n: number of jumps that happened before the target of the jump line

[0,n] -> int


def num_jumps_before(target): 
   pass

jump 3 -> jump 3
jump 7 -> 1 * 2 + 7
jump 13 -> 2 * 2 + 13 



Primitive types:
String
Integer
 
Instructions: 
Push <PRIMITIVE> :=> Add <PRIMITIVE> to the top of the stack (+1 item)
Pop              :=> Top of the stack is removed    (-1 item)
Print_and_pop    :=> Prints the top of the stack to stdout, and then removes it (-1 items)
Add              :=> Top 2 items of the stack are popped off, added, and the result is pushed (Integer +, String concat, convert Integer to String if necessary) (-1 item)
Jump         <INSTR_INDEX> :=> Continue executing at line <INSTR_INDEX> (+0 items)

"""

def run_the_program(program):
    index = 0
    stack = []
    while index >= 0 and index < len(program):
        instruction, param = program[index]
        if instruction == 'Push:
            stack.append(param)
        
        if instruction == 'Pop':
            stack.pop(-1)
            
        if instruction == 'Print_and_pop':
            print(stack[-1])
            stack.pop(-1)
            
        if instruction == 'Add':
            if len(stack) < 2:
                raise Error
            last = stack.pop(-1)
            second_to_last = stack.pop(-1)
            if type(last) == int and type(second_to_last) == int:
                res = last + second_to_last
            else: res = str(last) + str(second_to_last)
            stack.append(res)
        
        if instruction == 'Jump':
            index = param

            

Input:
    Jump 0
    
    num_jumps_so_far = [0]
    
    Push Jumping
    print and pop
    Jump 0


def notifyJump(program):
    jumpsBefore = []
    num_jumps_so_far = 0
    for line in program:
        jumpsBefore.append(num_jumps_so_far)
        if line[0] == 'Jump':
            num_jumps_so_far += 1
            
    for inst, param in program:
        if inst == 'Jump': 
            result_program.append(('Push', "Jumping"))
            result_program.append(('Print_and_pop', None))
            result_program.append(('Jump', jumpsBefore[param] * 2 + param))
        else:
            result_program.append(('Jump', param))
    return result_program


input_program # came from some developer

run_the_program(input_program) # produces
# I am 5
# I am 5
# ...

modified_program = notifyJump(input_program)

run_the_program(modifie_program) # produces
# I am 5
# Jumping
# I am 5
# Jumping
    


