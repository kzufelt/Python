n=4000000
a, b = 0, 1
evenfib=[]
while a < n:
	a, b = b, a+b
	if a%2==0:
		evenfib.insert(0,a)
	



if __name__ == "__main__":
    import sys
print(sum(evenfib))
    
