sumAge = 0
averageAge = 0
oldestMale = 0
nameOldestMale = ''
totalWomenUnder20 = 0
for p in range(1, 5):
    print('----- PERSON {} -----'.format(p))
    name = str(input('Nome: ')).strip()
    age = int(input('Age: '))
    gender = str(input('Gender [M/F]: ')).strip()
    sumAge += age
    if p == 1 and gender in 'Mm':
        oldestMale = age
        nameOldestMale = name
    if gender in 'Mm' and age > oldestMale:
        oldestMale = age
        nameOldestMale = name
    if gender in 'Ff' and age < 20:
        totalWomenUnder20 += 1
averageAge = sumAge / 4
print('The average age of the group is \033[1;33m{}\033[m years old'.format(averageAge))
print('The oldest male has \033[1;31m{}\033[m years old and his name is \033[1;31m{}\033[m'.format(oldestMale, nameOldestMale))
print('There is/are \033[1;35m{}\033[m female(s) under 20 years old'.format(totalWomenUnder20))

