n=600851475143
a=0
pfactor=[]
while a < n:
	a=a+1
	if n%a==0:
		pfactor.insert(0,a)
		n=n/a
	



if __name__ == "__main__":
    import sys
print(pfactor[0])
    
