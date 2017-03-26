#!/usr/bin/python3
# -*- coding: utf-8 -*-
# debug_example.py	
# 
#  --------------------------------
#  Output with debugger OFF
#  --------------------------------
# T:\user\dev\Github\dev_setup>debug_example.py
# example using the python debugger pdb
# 1  *  3  =  3
# 1  *  6  =  6
# 3  *  3  =  10  <-- Wrong answer
# 3  *  6  =  18
# 5  *  3  =  16  <-- Wrong answer
# 5  *  6  =  30
# 7  *  3  =  21
# 7  *  6  =  42
# 9  *  3  =  27
# 9  *  6  =  54

#  --------------------------------
#  Output with debugger on
#  --------------------------------
# T:\user\dev\Github\dev_setup>debug_example.py
# example using the python debugger pdb
# l(ist) - Displays 11 lines around the current line
# s(tep) - Execute the current line, stop at the first possible occasion.
# n(ext) - Continue execution until the next line in the current function is reached or it returns.
# b(reak) - Set a breakpoint (depending on the argument provided).
# r(eturn) - Continue execution until the current function returns.
# > t:\user\dev\github\dev_setup\debug_example.py(32)main()
# -> for length in range(1,10, 2):
# (Pdb) l
 # 27         print('n(ext) - Continue execution until the next line in the current function is reached or it returns.')
 # 28         print('b(reak) - Set a breakpoint (depending on the argument provided).')
 # 29         print('r(eturn) - Continue execution until the current function returns.')
 # 30         pdb.set_trace()  # comment this line out to see program run
 # 31
 # 32  ->     for length in range(1,10, 2):
 # 33             for width in range(3,8, 3):
 # 34                 ans = area(length,width)
 # 35                 if ans != length*width:
 # 36                     print(length , ' * ', width, ' = ', ans, ' <-- Wrong answer')
 # 37                 else:
# (Pdb)



import pdb
import random
    

def main():
    print('example using the python debugger pdb')
    print('l(ist) - Displays 11 lines around the current line')
    print('s(tep) - Execute the current line, stop at the first possible occasion.')
    print('n(ext) - Continue execution until the next line in the current function is reached or it returns.')
    print('b(reak) - Set a breakpoint (depending on the argument provided).')
    print('r(eturn) - Continue execution until the current function returns.')
    #pdb.set_trace()  # comment this line out to see program run
    
    for length in range(1,10, 2):
        for width in range(3,8, 3):
            ans = area(length,width)
            if ans != length*width:
                print(length , ' * ', width, ' = ', ans, ' <-- Wrong answer')
            else:
                print(length , ' * ', width, ' = ', ans)
            
    
    
def area(length, width):   
    """
    This is the entry point where you want to 
    start debugging form
    """
    a = length * width
    if  random.randint(0, 10) > 9:
        a += 1
    return a
    
    
    
if __name__ == "__main__":
    main()
    