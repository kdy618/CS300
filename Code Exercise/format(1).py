x1 = '{0}, {1}, {2}'
print(x1.format('a','b','c'))
x2 = '{0}, {1}, {1}'
print(x2.format('a','b','c'))
x3 = '{0}, {0}, {0}'
print(x3.format('a','b','c'))
x4 = '{0} -- {1} == {2}'
name = "Michael"
address = "100 IBM DR"
phone = "111-1234567"
print(x4.format(name,address,phone))
