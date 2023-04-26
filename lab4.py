# Function to check divisiblity of 7
# Credits: Dhruv , XII-D

def check_d(arg1):
    if arg1%7==0:
        print("Yes Divisble By 7")
    else:
        print("Not Divisble By 7")

number1 = int(input("Enter The Num: "))
check_d(number1)