# Program To Calc Compound Interest
# Credits: Dhruv , XII-D

def calc_compund(principal_amount,rate,time,number_of_times):
    return "Result: "+ str(principal_amount*(1+rate/number_of_times)*number_of_times*time)

principal_amount = int(input("Principal Amount : "))
rate = int(input("Rate: "))
time = int(input("Time: "))
number_of_times = int(input("Number Of Times: "))

print(calc_compund(principal_amount,rate,time,number_of_times))