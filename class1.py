#strings in python
name="Tomisin Adebiyi"
print(name[0])


'''
#python strings are immutable

name[3]="c"
'''

#we can convert python strings
num1 = "55"
print(type(num1))
num2 = int(num1)
print(type(num2))

'''
num="55"
print(type(int(num)))


#object references
x='blue'
y='green'
z=x
#print(x,y,z)

#we can rebind the variables:
z=y
#print(x,y,z)
x=z
print(x,y,z)

#python keywords
#and exec not
#assert finally or
#break for pass
#continue global raise
#def if return
#del import try
#elif in while
#else is with

route=1000
print(route, type(route))
route="north"
print(route, type(route))


collection data type
1. lists: -mutable

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
days[0] = 'Aje'
print(days)

words=['book', False, 'wednesday', 234]
words[2]=True
print(words)

#tuples:
countries=('Nigeria', 'The UK', 'Togo', 'Australia')
#they are unmutable:
print(countries)

print(len("Bolaji"))
print(len(["Monday", "Tuesday", "False", 501]))

true='God is good'
X=['zebra', 49, -987, "monkey", true]
x.append("more")
print(x)

'''