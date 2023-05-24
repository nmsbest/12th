# Write a func which transposes a list of numbers which are divisible by 5 to new stack.
# Credits: Dhruv , XII-D

original_list = []
refined_list = []

def add():
    n = int(input("How many numbers do you want to enter: "))
    for i in range(n):
        num = int(input("Number: "))
        original_list.append(num)
    print(original_list,refined_list)

def refine():
    for i in original_list:
        if i%5 == 0:
            refined_list.append(i)
    print(original_list,refined_list)
    
add()
refine()