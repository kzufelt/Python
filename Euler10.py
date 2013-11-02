#Sum of all the primes below two million
import time

def isprime(number):
	primeq=0
	iter=0
	for x in range(2,number//2+1):
		iter=iter+1
		if number%x==0:
			#print(number, " is divisible by ", x)
			return False
		elif number%x!=0:
			#print(number, " was divided by ", x)
			primeq=primeq+1
	#print(number, " is prime.")
	if primeq==iter:
		return True
	return False

def foo(q):
	start=time.time()
	currentnum=1
	sum=0
	while currentnum<q:
		currentnum=currentnum+1
		if isprime(currentnum):
			sum=sum+currentnum
		if currentnum%100000==0:
			timeelapsed=time.time()-start
			print("Time elapsed: ", timeelapsed)
			print("Completed to ", currentnum)
	print(sum)
	return

foo(2000000)

if __name__ == "__main__":
    import sys
