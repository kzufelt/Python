#10001st prime
primenum=0
currentnum=1
while primenum<10001:
	currentnum=currentnum+1
	primeq=0
	for x in range(currentnum-2):
		if currentnum%(x+2)==0:
			break
		
		elif currentnum%(x+2)!=0:
			primeq=primeq+1
		
	
	if primeq>(currentnum-3):
		primenum=primenum+1
		if primenum%1000==0:
			print('Found the first', primenum, 'primes.')
		
	





if __name__ == "__main__":
    import sys
print(currentnum)
