#Indexing in string
var = 'Hello World!'
print ("var      --> ", var)
print ("var[0]   --> ", var[0])
print ("var[1:5] --> ", var[1:5])
print ("var[:-5] --> ", var[:-5])

#String length, upper, lower
var = 'Hello World!'
print ("String --> ", var)
print ("Length --> : ", len(var))
print ("Upper  --> : ", var.upper())
print ("Lower  --> : ", var.lower())

# String formatting
name=input("Enter your name: ")
age=int(input("Enter your age : "))
price=float(input("Enter the book price: "))
s="\nYour name is %s, age is %d and book price is %f" %(name.upper(),age,price)
print (s)

# String in Triple Quotes
para_str = """This is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print (para_str)

#String strip
var =" Indian   Army    "

print("String    --> ", var)
print("Length    --> ", len(var))
print("var strip --> ", var.strip())
print("Length of var after strip --> ", len(var.strip()))

#String split
var =" Indian,   Army    "

print("String    --> ", var)
print("Length    --> ", len(var))
print("var split --> ", var.split())
print("var split --> ", var.split(' '))
print("var split --> ", var.split(','))

# Strip + Split
print("var split --> ", var.strip().split(','))

#Count in string
var=" Indian Army    "
print ("String       --> ", var)
print ("Count of ' ' --> ", var.count(' '))
print ("Count of 'a' --> ", var.count('a'))
print ("Count of 'n' --> ", var.count('an'))

# Reverse a String
var="Indian Army"
print ("String    --> ", var)
print ("var[::1]  --> ", var[::1])
print ("var[::2]  --> ", var[::2])
print ("var[::-1] --> ", var[::-1])
print ("var[::-2] --> ", var[::-2])

var=var[::-1]
print ("var after reverse --> ", var)

#Palindrome
s1="Indian Army"
s2="malayalam"
s3="madam"
s4="teacher"
print ("s1 --> ", s1==s1[::-1])
print ("s2 --> ", s2==s2[::-1])
print ("s3 --> ", s3==s3[::-1])
print ("s4 --> ", s4==s4[::-1])