from asyncio import Condition
from lib2to3.fixer_base import ConditionalFix


i = 10 
if i > 15: 
    print("10 is less than 15") 
print("I am Not in if") 

num = -5
if num > 0:
    print("The number is positive.")
else:
    print("The number is negative.")
    
    
   
# python program to illustrate nested If statement 
  
i = 10
if (i == 10): 
    
    #  First if statement 
    if (i < 15): 
        print("i is smaller than 15") 
          
    # Nested - if statement 
    # Will only be executed if statement above 
    # it is true 
    if (i < 12): 
        print("i is smaller than 12 too") 
    else: 
        print("i is greater than 15") 
        
        
# if Condition:
#    # Executes when condition1 is true
#    if Condition: 
      # Executes when condition2 is true
   # if Block is end here
# if Block is end here


# if condition1:
#     # code to execute if condition1 is true
# elif condition2:
#     # code to execute if condition1 is false and condition2 is true
# elif condition3:
#     # code to execute if condition1 and condition2 are false, and condition3 is true
# else:
#     # code to execute if all conditions are false
    
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print("Your grade is:", grade)

# Python program to illustrate if-elif-else ladder 
#!/usr/bin/python 
  
i = 20
if (i == 10): 
    print("i is 10") 
elif (i == 15): 
    print("i is 15") 
elif (i == 20): 
    print("i is 20") 
else: 
    print("i is not present") 