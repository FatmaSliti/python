user = {
    'name': 'Fatma',
    'age': 22,
    'Country': 'Tunisia',
    'skills': ['HTML', 'CSS', 'JS', 'ReactJs'],
    'rating': 1,
    # 'name': 'Fatouma'
}

print(user)
print(user['Country']) #Tunisia
print(user.get('Country'))

print(user.keys()) #dict_keys(['name', 'age', 'Country', 'skills', 'rating'])   
print(user.values()) #dict_values(['Fatma', 22, 'Tunisia', ['HTML', 'CSS', 'JS', 'ReactJs'], 1])


#2D Dictionary

languages = {
    'one': {
        'name': 'html',
        'progress': '85%',
    },
    'Two': {
        'name': 'CSS',
        'progress': '86%'
    },
    'Three': {
        'name': 'JS',
        'progress': '80%'
    }
}

print(languages)
print(languages['one']) #{'name': 'html', 'progress': '80%'}
print(languages['Three']['progress'])

#Dictionary Length

print(len(languages)) #3
print(len(languages['Two'])) #2


# Create Dictionary from variables

frameworkOne = {
    'name': 'Vuejs',
    'progress': '80%',
}

frameworkTwo = {
    'name': 'ReactJs',
    'progress': '80%',
}

frameworkThree = {
    'name': 'Angular',
    'progress': '80%',
}

allFrameworks = {
    'one': frameworkOne,
    'two': frameworkTwo,
    'three': frameworkThree
}

print(allFrameworks)

