def gcd(m,n):
	while (m%n)!=0 :
		oldm=m
		oldn=n
		m=oldn
		n=oldm%oldn
	return n

print (gcd(10,20))
print (gcd(5,4))
print (gcd(21,14))

