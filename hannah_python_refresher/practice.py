#practice python programming/conventions

#elif statements
#elif and else is optional, : must indents following line
grade = 99

if grade > 90:
    print("A")
elif grade > 60:
    print("B")
elif grade > 50:
    print ("C")
else:
    print("FAIL")

#other evaluations
    #true and false
#FALSE
print(5>9)
#TRUE
print('matt' == 'matt')
#FALSE
print('matt' != 'matt')

#TRUE - checks is matt is instance of a string
print(isinstance('matt', str))

#can use 'and' 'or' 'not', '&' etc


#iterations/for loops
#python creates number variable (e.g for i in...,i++)
for number in [1,2,3,4]:
    print(number)

#range, prints same result as above
for number in range(1,5):
    print(number)

myList = list(range(5)) #includes 0,1,2,3,4
print(myList)

#indexing:
animals = ["dog", "cat", "bird"]
for index, value in enumerate(animals):
    print(index, value)

#lists
#list from literals
names = ['john', 'paul', 'ringo']
print(names)
#list from constructor
vals = list(range(4))

#list is mutable - can be changed
#append changes what is in the list
names.append('george')
print(names)
#fetch index number
print(names.index('ringo'))


#slicing :3 doesn't incluyde 4th value at index 3
print(names[0:3])
print(names[:3])
print(names[3])

#stride
#names [::-1] - reverse order

#comprehension - looping/mapping...
#items in names that are legnth 4, adds to new list names2, make title format paul = Paul
names2 = []
for name in names:
    if len(name) == 4:
        names2.append(name.title())
print(names2)


#dictionaries
hash('name')
#lists are not hash-able
#literals vs constructor
types = {'name' : str, 'age':int, 'address':str}
types2 = dict(name=str, age=int, adress=str)
#dictionary fast for lookup
#dictionary now remembers order of key insertion


#functions
def add(x,y):
    #doc string
    """This adds two values"""
    return x + y

#calling function
print (add(1,55))


