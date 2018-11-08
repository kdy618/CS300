'''The specifications for this program are identical to those for build 3, 
except that you are to use the format() function. 
As much as possible. This will require repeating code, 
but without the need to edit all of it each time.'''

x = '\nGreetings from a beginning Python programmer.\nDo you want to be address as ...\n'
y = 'or'
z = '.......................................======>'
z0 = '?'
name1_Full = '{0} {1} {2}'
name1_FirstLast = '{0} {1}'
name1_Name = '{0}'

print(x)
print(z + name1_Full.format('Jane', 'Margaret', 'Doe') + z0)
print(z + name1_FirstLast.format('Jane', 'Doe') + z0)
print(z + 'Mr./Ms. ' + name1_Full.format('Jane', 'Margaret', 'Doe') + z0)
print(z + 'Dear '+ name1_Name.format('Jane') + z0)
print(y)
print(z + name1_Full.format('Doe,', 'Jane', 'Margaret') + z0 + '\n')
print(z + name1_Full.format('Archibald', 'Montague', 'Abercrombie') + z0)
print(z + name1_FirstLast.format('Archibald', 'Abercrombie') + z0)
print(z + 'Mr./Ms. ' + name1_Full.format('Archibald', 'Montague', 'Abercrombie') + z0)
print(z + 'Dear ' + name1_Name.format('Archibald') + z0)
print(y)
print(z + name1_Full.format('Abercrombie,', 'Archibald', 'Montague') + z0 + '\n')
print(z + name1_Full.format('Cleopatra', 'Anastasia', 'Montgomery') + z0)
print(z + name1_FirstLast.format('Cleopatra', 'Montgomery') + z0)
print(z + 'Mr./Ms. ' + name1_Full.format('Cleopatra', 'Anastasia', 'Montgomery') + z0)
print(z + 'Dear ' + name1_Name.format('Cleopatra') + z0)
print(y)
print(z + name1_Full.format('Montgomery,', 'Cleopatra', 'Anastasia') + z0)
