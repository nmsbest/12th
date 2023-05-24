"""
Write a func AddCustomer(customer) in py to add a new customer info into the stack (list) CStack and display the info
Write a func DeleteCustomer() to delete a Customer info from a list of CStack
The function delete the name of customer from the stack

eg: if the stack contains ['abhinav','vimnak'] the output should be
Vimnak
Abhinav
"""
# Credits: Dhruv , XII-D

customer = []

def AddCustomer():
    n = int(input("How many customer do you want to add : "))
    for i in range(n):
        newCustomer = str(input("Customer you want to add : "))
        customer.append(newCustomer)
        print(customer)

def DeleteCustomer():
    newCustomer = str(input("Customer you want to remove : "))
    customer.remove(newCustomer)
    print(customer)

AddCustomer()
DeleteCustomer()
