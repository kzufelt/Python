n=1000
palindrome=[]
palin=0
for x in range(n):
	for y in range(x):
		t=str(x*y)
		for z in range(int(len(t)/2)):
			if t[z]==t[-1-z]:
				palin=palin+1
			
		
		if palin==int(len(t)/2):
			palindrome.insert(0,int(t))
		
		palin=0
	

	

palindrome = list(set(palindrome))
palindrome.sort()


if __name__ == "__main__":
    import sys
print(palindrome[-1])
    
