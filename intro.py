#Strings in Python
'''
name="Bolaji Lawanson"
print(name[0])
'''
'''
#python strings are immutable
name[3]="c"
'''
#we can convert python strings to other types
'''
num1 = "55"
print(type(num1))
num2 = int(num1)
print(type(num2))
'''
'''
num="55"
print(type(int(num)))
'''

#Object References
x='blue'
y='Green'
z=x
#print(x,y,z)

#we can rebind the variables:
z=y
#print(x,y,z)

x=z
print(x,y,z)

#Python keywords
#And exec Not
#Assert finally or
#Break for pass
#Class from print
#Continue global raise
#def if return
#del import try
#elif in while
#else is with
'''
route=1000
print(route, type(route))
route="North"
print(route, type(route))
'''

'''
Collection Data Types
1. Lists: -mutable
'''
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
days[0] = 'Aje'
#print(days)

words=['book', False, 'Wednesday', 234]
words[2] = True
#print(words)

#2. Tuples:
countries=('Nigeria', 'The UK', 'Togo', 'Australia', 1)
#they are unmutable:
#countries[2]="Lagos" 
print(countries)

#Python's sequence types are sized - they can be passed to the len() function
true="God is good"
x=['zebra', 49, -987, "monkey", true]
x.append("more")
print(x)