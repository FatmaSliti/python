monthConversions = {
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March',
    'Apr': 'April', 
    'May': 'May',
    'Jun': 'June',
    'Jul': 'July',
    'Aug': 'August',
    'Sep': 'September',
    'Oct': 'October',
    'Nov': 'November',
    'Dec': 'December'
}

# print(monthConversions['Jan'])

# print(monthConversions.get('Dec'))
print(monthConversions.get('jk', 'Not a valid key'))


monthConversionsUsingNumbers = {
    0: 'January',
    1: 'February',
    2: 'March',
}

# print(monthConversionsUsingNumbers[0])
print(monthConversionsUsingNumbers.get(0))