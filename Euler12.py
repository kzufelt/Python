#First triangle number to have over five hundred divisors
import time
import math

def isprime(number):
	primeq=0
	iter=0
	for x in range(2,number//2+1):
		iter=iter+1
		if number%x==0:
			return false
		elif number%x!=0:
			primeq=primeq+1
	if primeq==iter:
		return true
	return false

for j in range(100):
	triangle=0
	for i in range(j):
		triangle=triangle+i
	isprime(triangle)
	



if __name__ == "__main__":
    import sys
