'''
#There are different types of data structures; List, Tuples and Dictionaries amongst many.
list1 = ['Mathematics', 'language', 'science', '2000', 'False', 'HealthEducation']
#accesing the nth item
print(list1[2])

#updating the list
list1[4] = True
print(list1)

#deleting items from a list
del list1[2]
print(list1)

#multiplication and  concatenation
object1 = list1 + ['Agric', '10.7']
print(object1)

print(['Agric', '10.7'] * 3)

#length of list1
print(len(list1))
#membership
print('Agric' in object1)

#iteration
print('start iteration')
for x in list1:
	print(x)

print('Start from here')
for x in list1:
	if(list1.index(x) < 3):
		print(x)


list1 = ['Mathematics', 'language', '2000', 'False', 'HealthEducation']
for x in list1:
	print(x, end=" and ")

list1 = ['Mathematics', 'language', '2000', 'False', 'HealthEducation']
print('Start from here')
for x in list1:
	if(list1.index(x) <= 3):
		print(x, end=" and ")
	else:
		print(x)

#indexing
list1= ['Mathematics', 'language', 2000, True, 'HealthEducation']
print(list1[-2])
print(list1)
print(list1[2:])
print(list1[:2])
print(list1[1:4])

#max
list2= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',]
print(min(list2))
print(max(list2))

#converting tuple to a list
tuple1 =(234, "C++", False, 'Python')
object2= list(tuple1)
print(object2)

#append
object2= [234, 'C++', False, 'Python']
object3=object2.append('C#')
object4 = object2 + ['C#']
print(object4)
print(object3)

#countc
list3 = [234, 'C++', False, 'Python', 'C++', 'C#']
print(list3.count('C++'))

print([234, 'C++', False, 'Python', 'C++', 'C#'].count('Python'))
print([234, 'C++', False, 'Python', 'C++', 'C#'].count('Jhon'))

#extending a range into a list
print(range(5))
for i in range(5):
	print(i, end=" ")
'''

'''
list4= list(('a','b','c','d'))
print(list4)
new= list4.extend(range(5))
print(new)
print(list4)
'''

'''
#index
names=['Bolaji', 'Aisha', 'Daniel', 'David', 'Taofeeq']
print("first occurence of aisha", names.index('Aisha'))

#pop
subjects=['maths', 'english', 'science', 'culture', 'religion', 'language']
print(subjects.pop())
print(subjects.pop())
print(subjects.pop())
print(subjects.pop())
print(subjects.pop())
print(subjects.pop())
print(subjects.pop())
'''

'''
#remove(): removes the last item but returns NONE
subjects=['maths', 'english', 'science', 'culture', 'religion', 'language']
holder1=subjects.pop()
holder2=subjects.remove('english')
print(holder1)
print(holder2)

#reverse: reverses the list and returns none
subjects=['maths', 'english', 'science', 'culture', 'religion', 'language']
holder3= subjects.reverse()
print(holder3)
print(subjects)

#sort
subjects=['maths', 'english', 'science', 'culture', 'Religion', 'language', '43']
print(subjects.sort())
print(subjects)
'''
'''
#Dictionaries
states_pop = {"Lagos":3456789, "Kano":4567890, "Abuja":1234567, "Port Harcourt":2345678}
print(states_pop['Kano'])
states_pop['Ogun']= 2345687
print(states_pop)

en_yor = {'one':'ookan', 'two':'eeji', 'three':'eeta', 'four':'eerin', 'five':'aarun'}
print(en_yor['two'])

yor_ibo = {'ookan':'otu', 'eeji':'abuo', 'eeta':'ato', 'eerin':'ano', 'aarun':'ise'}
print(yor_ibo['eeta'])

print(yor_ibo[en_yor['one']])
'''
#Rules
#we can't use mutable types as key
#dic = {[1,2,3]: 'abc'}
#dic = {'abc': [1,2,3]}

#operations on Dictionaries
#len (), del (k), k in d, k not in d
#print('abc' in dic)
#del dic['abc']
#print(dic)
#print(len(dic))

'''
morse = {
	'A': 'qw',
	'B': 'qwer',
	'C': 'qwerty',
	'D': 'qwertyui',
	'E': 'qwertyuiop',
	'1': 'as',
	'2': 'asdf',
	'3': 'asdfghj',
	'4': 'asdfghjkl',
	'5': 'asdfghjklzx'
}
from datastructures import morse
print(len(morse))
'''

#pop()
en_yor = {'one':'ookan', 'two':'eeji', 'three':'eeta', 'four':'eerin', 'five':'aarun'}
#print(en_yor.pop('one'))
#print(en_yor.pop('three'))
'''
word = (input('Type something in English').lower())
#new_word=word.lower()
en_yor = {'one':'ookan', 'two':'eeji', 'three':'eeta', 'four':'eerin', 'five':'aarun'}
yor_ibo = {'ookan':'otu', 'eeji':'abuo', 'eeta':'ato', 'eerin':'ano', 'aarun':'ise'}
print(yor_ibo[en_yor[word]])
'''
#if a pair cannot be popped, a key error is raised
#print(en_yor.pop('six'))
#en_yor.pop('six', 'eefa')

'''
#popitem
print(capitals.popitem())
print(capitals.popitem())
print(capitals.popitem())
print(capitals.popitem())
print(capitals.popitem())
print(capitals)

#we can prevent the errors from passing non-existent keys using the membership operator
if 'Rivers' in capitals:
    print(capitals['Rivers'])

#alternative, get() can be used
capitals = {'Nigeria':'Abuja', 'Ghana':'Accra', 'Togo':'Lome', 'South Africa': 'Johannesburg', 'Mali':'Bamako'}
print(capitals.get('Rivers'))
'''
'''
#copy():
capitals1 = {'Nigeria':'Abuja', 'Ghana':'Accra', 'Togo':'Lome', 'South Africa': 'Johannesburg', 'Mali':'Bamako'}
capitals2 = {'United Kingdom':'London', 'Russia':'Moscow', 'Sweden':'Stockholm'}
updated_dic = capitals1.update(capitals2)
print(updated_dic)
print(capitals1)

#iterating over a dictionary:
#print all the items in the updated capitals1 dictionary
'''

#conversion Between Lists and Dictionaries:
capitals1 = ("Nigeria":"Abuja", "Ghana":"Accra", "Togo":"Logo", "South-Africa":"Johannesburg", "Mali":"Bamako"),

print((type(capitals1)))
list1 = [capitals1]
print(list1)
print(type(list1))
print(list1[1])


#iterating over a dictionary
#print all the items in the updated capitals1 dictionary
capitals1 = {'Nigeria': 'Abuja', 'Ghana': 'Accra', 'Togo': 'Lome', 'South Africa': 'Johannesburg', 'Mali': 'Bamako', 'United Kingdom': 'London', 'Russia': 'Moscow', 'Sweden': 'Stockholm'}
for cities, towns in capitals1.items():
    print(cities+": "+towns)


