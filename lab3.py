# Py Program to find and display the prime number bw 2 to N . Pass M as arg to method
# Credits: Dhruv , XII-D

def get_prime_number(num1):
    for num in range(2, num1 + 1):
        if num > 1:
            for i in range(2, num+1):
                if (num % i) == 0:
                    break
            else:
                print(num)

number1 = int(input("Enter The Num: "))
get_prime_number(number1)