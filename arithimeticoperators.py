#overloaded fxn is a function that has the same identifier but different functions/action/activities
'''
name="John"
name += " Mike"
print(name)
'''
'''
#print(list1) will return an object bcos an int is not iterable
list1= ["Mango", 'Orange', 'Cashew', 'Onion']
#list1 += 1
list2= ['tomato', '20']
print(type(list2))
print(list1 + list2)
list2+= ['cherry', 'bananas']
print(list2)
'''
'''
#returns the sum of all valid inputs,
#drops every invalid input politely
total=0
count=0
while True:
 	try: 
 		line=input("enter a number")
 		if line:
 			try:
 				number=int(line)
 			except ValueError as ve:
 				print(ve)
 				continue
 		total += number
 		count += 1
 		print(total)
 	except EOFError:
 		break
'''

#Using Functions:
#methods are functions declared inside a class
'''
def get_int():
		try:
			i = int(input("Enter a number or something convertible"))
			print("Your age is ",i)		

		except ValueError as ve:
			print(ve)
get_int()
'''

'''
def add(b,a):
	#a=float(input("Enter the first number"))
	#b=float(input("Enter the second number"))
	print(a-b)
add(19,20)
'''

from datastructures import morse
print(len(morse))