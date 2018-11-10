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
3.
After a blank line, the same output, but applied to Archibald Montague Abercrombie
4.
After a blank line, the same output, but applied to Cleopatra Anastasia Montgomery
'''

x = '\nGreetings from a beginning Python programmer.\n'
    'Do you want to be address as ...\n'
y = 'or'
z = '.......................................======>'
z0 = '?'
name1 = 'Jane'
middleName1 = 'Margaret'
lastName1 = 'Doe'
name2 = 'Archibald'
middleName2 = 'Montague'
lastName2 = 'Abercrombie'
name3 = 'Cleopatra'
middleName3 = 'Anastasia'
lastName3 = 'Montgomery'

print(x)
print(z + name1 + " " + middleName1 + " " + lastName1 + z0)
print(z + name1 + " " + lastName1 + z0)
print(z + "Mr./Ms. " + name1 + " " + middleName1 + " " + lastName1 + z0)
print(z + "Dear " + name1 + z0)
print(y)
print(z + lastName1 + "," + name1 + " " + middleName1 + z0 + "\n")
print(z + name2 + " " + middleName2 + " " + lastName2 + z0)
print(z + name2 + " " + lastName2 + z0)
print(z + "Mr./Ms. " + name2 + " " + middleName2 + " " + lastName2 + z0)
print(z + "Dear " + name2 + z0)
print(y)
print(z + lastName2 + "," + name2 + " " + middleName2 + z0 + "\n")
print(z + name3 + " " + middleName3 + " " + lastName3 + z0)
print(z + name3 + " " + lastName3 + z0)
print(z + "Mr./Ms. " + name3 + " " + middleName3 + " " + lastName3 + z0)
print(z + "Dear " + name3 + z0)
print(y)
print(z + lastName3 + "," + name3 + " " + middleName3 + z0)
