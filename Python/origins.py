fathersDict = {'Harold Abelson': 'Logo',
               'Andrei Alexandrescu': 'C++',
               'Alfred Vaino Aho': 'AWK',
               'Guido van Rossum': 'Python',
               'Jeremy Ashkenas': 'CoffeeScript',
               'Walter Bright': 'D',
               'John George Kemeny': 'Basic',
               'Peter Naur': 'Algol',
               'Don Syme': 'F',
               'Kenneth Eugene Iverson': 'APL',
               }
print("Choose mode type.")
print("Enter 'search' or 'sort': ", end='')
choose = input()
print()

if choose == 'sort':
    sortList = sorted(fathersDict.keys())
    for name in sortList:
        print(name, " - ", fathersDict[name])
elif choose == 'search':
    print("Enter developer's name: ", end='')
    name = input()
        for father in fathersDict.keys():
        if father == name:
            print(fathersDict[name], "was created by", name)
else:
    print("Incorrect mode type. Try again")

