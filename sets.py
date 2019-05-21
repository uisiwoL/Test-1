#creating sets
x = set("A python set")
print(type (x))
#passed a list to the inbuilt set() function

y = set(["Python", "C++", "Java", "Javascript", "PHP"])
print(y)


#when a tuple contains a repeated item is passed to the set() fxn
states = set(("Lagos", "Benin", "Onitsha", "Kaduna", "Benin", "Bayelsa"))
print(states)
states.add("Rivers")
print(states)

#we cannot include mutable objects during set creation
#classes = set("Js1", ["ss1", 'ss2', 'ss3'], 'js2', 'js3')
'''
#frozen sets
food = frozenset(['egg', 'jam', 'bread', True])
print(food)
print(food.add("butter"))
'''

#using the curly brace
states = {"Lagos", "Benin", "Onitsha", "Kaduna", "Benin", "Bayelsa"}

#sets operations
#add()
colors = {"Red", "Green", "Blue"}
print(colors.add("Brown"))
print(colors)



#clear()
states = {"Lagos", "Benin", "Onitsha", "Kaduna", "Benin", "Bayelsa"}
#print(states.clear())
print(states)

#remove()
print(states.remove("Onitsha"))
print(states)
2
#copy()
more_states = {"ogun", "Imo", "Nasarawa", "Kaduna", "Adamawa"}
more_states_backup = more_states.copy()
print(more_states_backup)

#differences
A = {"Tomi", "Daniel", "Ejiro", "Salah"}
B = {"Daniel", "Mohammed", "Bolaji", "Kayode"}
#print(A - B)
print(A.difference(B))
#print(B - A)
print(B.difference(A))

# difference_update()
x = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
y = {'c', 'f', 'b'}
z = {'e', 'd', 't', 'o'}
differ = x-y-z
print(differ)
x.difference_update(y)
print(x)

#discard()
x = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
x.discard('d')
print(x)

#intersection
x = {'a', 'b', 'c', 'd', 'e'}
y = {'c', 'd', 'e', 'f', 'g'}
print(x & (y))
print(x.union(y))

#disjoint()
print(x.isdisjoint(y))

#subset()
x = {'a', 'b', 'c', 'd', 'e'}
y = {'c', 'd'}

print(y.issubset(x))
print(y < x)
print(x.issubset(y))
print(x > y)



#keyword parameters
def sum(a, b, c=0, d=0):
    return a-b+c-d
print(sum(12,4))
print(sum(12,4,5))


#variable scoping: by def, variables defined in a fxn are local to that
def f():
    print(s)
s="python"
f()

def f():
    #print(s)
    s='perl'
    print(s)
s="python"

def f():
    s = 'closure'
    print(s)
f()

def f():
    global s
    print(s)
    s='dog'
    print(s)
s='cat'
f()
print(s)

#arbirary number of parameters
def arithmetic_mean(first, *values):
    return (first + sum(values)) / (1 + len(values))
print(arithmetic_mean(45, 32, 89, 78))


#solve geometric proressions(r>1)
def sumgp():
    a=float(input('Enter first term'))
    r=float(input('Enter common ratio'))
    n=float(input('how many terms'))

    print((a*(pow(r,n)- 1)) / (r-1))
sumgp()

def average(*values):
    print((sum(values)))

#recursive functions
def factorial(n):
    if n == 1:
        return 1
    else:
        n * factorial(n-1)
print(facto(5))

