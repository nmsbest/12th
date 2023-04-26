# Function Menu Driven Airthmetic Operation
# Credits: Dhruv , XII-D

def get_result(type_of_operation,num1,num2):
    if type_of_operation == "+":return num1+num2
    elif type_of_operation == "-":return num1-num2
    elif type_of_operation == "*":return num1*num2
    elif type_of_operation == "/":return num1/num2
    
ops = str(input("Ops: "))
num1 = int(input("Num1 : "))
num2 = int(input("Num2 : "))

print(get_result(ops,num1,num2))