message = "hello Python World!"
print(message)

message = "Hello python crash course!"
print(message)

name = "joseph niccoli"
print(name.title())
print(name.upper())
print(name.lower())

# Chapter 2
# 9/14/2020
first_name = "joe"
last_name = "niccoli"
full_name =(f"{first_name} {last_name}")
print(full_name)

print (f"Hello, {full_name.title()}!")

message = (f"Hello your name is {full_name.title()}!")

print(message)

# 9/15/2020
# f is for format it allows u to add variables into the string
message1 = (f"Hello  your name is \t\n {full_name.title()}!")
print(message1)

print("strip white spaces")
message2 = "    username:joeniccoli   "
print(message2)
print(message2.lstrip())
print(message2)
print(message2.strip())
print(message2)
print(message2.rstrip()) # this is temporary space removal
print(message2)
message2 = message2.strip() # permanant space removal 
print(message2)

# 9/16/2020
print(5+6)

MAX_CONSTRAINTS = 76 # constraints should be in all caps

print(MAX_CONSTRAINTS)

 
# The Zen of Python, by Tim Peters
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!


#chapter 3
#first List 

names = ['joe','anna','jeff','kris']
print (names)
print(names[2])
print(names[2].title())
print(names[-1]) # adding a negative to brackets allows u to get the values on the opposite side of the list
print(f"Hello  your name is \t\n {names[0].title()}!")


pop_name = 'joe'
print(names)
# pop removes the last item from the list
print(f"remove name {names.pop()} from the list")
print (names)

# (remove) removes the variables value from the list
names.remove(pop_name)
print(names)


names.append('jason') # adds the name to the end of the list append()
print (names)

names.insert(0,'kris') # inserts the name at the position desired in the list insert()
print(names)
names.insert(2, 'joe')
print(names)
del names[2]
print(f"the names that are left are {names}")


# sorts the list in alphabetical order sort()
names.sort()
print(names)

#9/17/2020
# temporary sorting
names2 = ['joe','anna','jeff','kris']
print(sorted(names2))
print (names2)
#reverse the list  reverse()
names2.reverse()
print(names2)

# find the length of the list len()
print(len(names2))


