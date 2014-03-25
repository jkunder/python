counter = 1
done = False
while counter <=5 and not done:
	print ("Hello")
        done = True
	counter=counter+1

for item in [1,2,5,4,8]:
	print item

for i in range(5):
	print i

mylist = []
wordlist = ['cat', 'dog', 'reindeer']
for aword in wordlist:
	for aletter in aword:
		if aletter not in mylist:
			mylist.append(aletter)
print mylist

x=90

if x > 100 :
	print (100)
elif x > 90 :
	print (90)
else :
	print (80)


print ('list comprehension')
sqlist=[x*x for x in range(10)]
print sqlist
print ('list comprehension with selection')
sqlist=[x*x for x in range(10) if x%2]
print sqlist

upper=[ch.upper() for ch in 'comprehension' if ch not in 'aeiou']
print upper

