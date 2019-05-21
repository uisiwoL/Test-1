'''
#identity:
a = ["today", "tomorrow", True, 0.5, False]
b = ["today", "tomorrow", True, 0.5, False]
print(a is b)
print(a is not b)
a=b
print(a is b)
print(a is not b)
'''

'''
#comparison
a=2
b=6
print(a<b)
print(a>b)

#in python we can chain comparison operators:
a=9
print(0 <= a <= 10)

print("three" < 4 )
#python is strongly dynamically typed. We don't need to supply the object type
'''
'''
#membership 
p = (4, "monkey", 10, -33, True)
print(2 in p)
print(2 not in p)

q = "Today is Tuesday"
print("Today" in q)
'''
'''
a = "Monday"
b = "Tuesday"
print(a and b)
print(a or b)
'''

'''

#			Control Flow Statements
#the if-else statement:
if condition1:
	pass
elif condion2:
	pass
...
else:
	pass
'''
'''
a=10
b=3
c=7
if (a>b and b<c):
	print("Very so")
	print(b+a+c)
elif(a<b or c>b):
	print("Not really true")
else:
	"Adunno"
'''


#The while Loop:to test if a condition returns true, more than once:
'''
lessThan5 = 0
while lessThan5 < 5:
	print("Still < 5")
	lessThan5 += 1
	if lessThan5==3:
		break
	print("Thank you")
print("finished")
'''
'''
lessThan5=0
while lessThan5 < 5:
	print("Still < 5")
	lessThan5 += 1
	if lessThan5==3:
		continue
	print("I'm waiting")
'''
'''
countries = ["Nigeria", "Ghana", True, 1000, "America"]
i=0
while i<len(countries):
	print(countries[i])
	i += 1
'''

'''
countries = ["Nigeria", "Ghana", True, 1000, "America"]
for cou in countries:
	print(cou)
'''

'''
for i in "abcdefghijklmnopqrstuvwxyz":
	if i in "aeiou":
		print(i, "is a vowel")
	else:
		print(i, "is a consonant")
'''
'''
v="today"
print(len(v))

v = input("Say something")
print(len(v))
'''

try:
	x=int(input("Enter a number"))
	ansa = x/2
	print(ansa)
except ValueError as err:
	print(err)
	
