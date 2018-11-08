'''
Intent: Begin to provide options for the form of one person to be addressed.

Postconditions: The following are on the console (excluding the numbering):
1.
Greetings from a beginning Python programmer.
2.
Do you want to be addressed as ...
.......................................======>Jane Margaret Doe?
.......................................======>Jane Doe?
.......................................======>Mr./Ms. Jane Margaret Doe?
.......................................======>Dear Jane?
or 
.......................................======>Doe, Jane Margaret?
'''

x = '\nGreetings from a beginning Python programmer.\nDo you want to be address as ...'
y = '.......................................======>'
z = 'or'
z0 = '?'
name = 'Jane'
middleName = 'Margaret'
lastName = 'Doe'

print(x)
print(y + name + " " + middleName + " " + lastName + z0)
print(y + name + " " + lastName + z0)
print(y + "Mr./Ms. " + name + " " + middleName + " " + lastName + z0)
print(y + "Dear " + name + z0)
print(z)
print(y + lastName + "," + " " + name + " " + middleName + z0)
