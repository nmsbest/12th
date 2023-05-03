# Py Program to find and display the prime number bw 2 to N . Pass M as arg to method
# Credits: Dhruv , XII-D

def find_primes_between(m, n):
    primes = []
    for num in range(2, n+1):
        if all(num%i!=0 for i in range(2, int(num**0.5)+1)):
            primes.append(num)
    return [p for p in primes if p >= m]

N = int(input("Enter the value of N: "))
M = int(input("Enter the value of M: "))
prime_numbers = find_primes_between(M, N)
print("Prime numbers between", M, "and", N, "are:", prime_numbers)