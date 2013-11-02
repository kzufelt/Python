#Difference between sum of squares and square of sums for first 100 numbers
sumsq=sqsum=sum1=0
for x in range(100):
	sumsq=sumsq+(x+1)**2
	sum1=sum1+(x+1)

sqsum=sum1**2
i=sqsum-sumsq




if __name__ == "__main__":
    import sys
print(sqsum)
print(sum1)
print(sumsq)
print(i)

    
