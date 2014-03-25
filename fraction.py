def gcd (x,y):
	while (x%y) != 0 :
		oldx=x
		oldy=y
		x=oldy
		y=oldx%oldy
	return y

class fraction :
	def __init__ (self,top, bottom):
		self.num=top
		self.den=bottom

	def show(self):
		print `self.num`+'/'+`self.den`

        def __str__ (self):
                if (self.den == 1) :
			return `self.num`
		return `self.num`+'/'+`self.den`

        def __add__ (self, otherfn):
		den = self.den * otherfn.den
		num = self.num*otherfn.den + otherfn.num*self.den
                divby = gcd(den,num)
                return `num/divby`+'/'+`den/divby`

	def __mul__ (self,otherfn):
		den = self.den * otherfn.den
		num = self.num * otherfn.num
                divby = gcd(den,num)
                return `num/divby`+'/'+`den/divby`

        def __eq__ (self, otherfn):
		den = self.den * otherfn.den
		mynum = self.num*otherfn.den 
		othernum = otherfn.num*self.den
		return mynum==othernum

num = fraction(3,4)
num1 = fraction(1,4)
print str(num) + '+' + str(num1) + '=' +  (num+num1)
print str(num) + 'x' + str(num1) + '=' +  (num*num1)
