'''
List: [1, 2, 'a', 3.14]

List comprehensions:

    [expr for val in collection]

    [expr for val in collection if <test>]

    [expr for val in collection if <test1> and <test2>]

    [expr for val1 in collection1 and val2 in collection2]

'''

# squares list example

squares = []

for i in range(1, 19):
    squares.append(i**2)
print(squares)

squares2 = [i**2 for i in range(1, 19)]
print(squares2)

###
remainders5 = [x**2 % 5 for x in range(1, 19)]
print(remainders5)

remainders11 = [x**2 % 11 for x in range(1, 19)]
print(remainders11)
