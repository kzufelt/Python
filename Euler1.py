a=[]
for b in range(1000):
	if b%3==0:
		a.insert(0,b)
	
	elif b%5==0:
		a.insert(0,b)
	

sum=0
for x in a:
	sum=sum+x


if __name__ == "__main__":
    import sys
print(sum)
    
