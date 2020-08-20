"""
Sophie Germain Prime
Write a program to print all sophie germain number less than n. 
A prime number p is called a sophie prime number if 2p+1 is also a prime number. 
The number 2p+1 is called a safe prime. 
For example 11 is a prime number and 11*2 + 1 = 23 is also a prime number 
so, 11 is sophie germain prime number . 
The first few Sophie German prime numbers are 
2, 3, 5, 11, 23, 29, 41, 53, 83, 89, 113, 131, 173, 179 ..

Application of Sophie Prime Numbers :
1. It is used in cryptography as safe primes become the factors of a secret key in RSA cryptosystem.
2. In the first version of AKS Primality Test, it is used to lower the worst case complexity .
3. It is used in the generation of Pseudo Random Number .
"""
def sieve(n, prime) : 
    p = 2
    while( p * p <= n ): 
        if (prime[p] == True) :
            for i in range(p * 2, n, p) : 
                prime[i] = False            
        p += 1
                  
def printSophieGermanNumber(n) : 
    prime = [True]*(2 * n + 1) 
    sieve(2 * n + 1, prime) 
    for i in range(2, n + 1) : 
        if (prime[i] and prime[2 * i + 1]) : 
            print( i , end = " ") 
print("Enter the No")
n = int(input())
printSophieGermanNumber(n) 