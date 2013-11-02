#Sum of all the primes below two million
import time
import math

def isPrime(n):
	if n==1:
		return False
	elif n<4:
		return True #2 and 3 are prime
	elif n%2==0:
		return False
	elif n<9:
		return True #we have already excluded 4,6 and 8.
	elif n%3==0:
		return False
	else:
		r=math.floor(math.sqrt(n)) 
		f=5
		while f<=r:
			if n%f==0:
				return False
			if n%(f+2)==0:
				return False
			f=f+6
	return True


def foo(q):
	start=time.time()
	currentnum=1
	sum=0
	while currentnum<q:
		currentnum=currentnum+1
		if isPrime(currentnum):
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
