#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.
import math
import re

def foo():
	for i in range(c,960):
		for j in range(b,i): 
			for k in range(a,j):
				if (pow(k,2)+pow(j,2)==pow(i,2) and i+j+k==1000):
					a2=k
					b2=j
					c2=i
					answer=a2*b2*c2
					print(a2)
					print(b2)
					print(c2)
					print(answer)
					if answer > 0:
            					return

a=3
b=4
c=5
answer=0
foo()


if __name__ == "__main__":
    import sys
