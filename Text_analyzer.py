from typing import Any

print('Welcome in Text Analyzer\n')
print('=' * 40)
print ('Author: Jaroslav Prejza\n')
print('=' * 40)
data = {'bob': '123','ann': 'pass123','mike': 'password123','liz': 'pass123'}

username = input('Please enter username: \n')
print()
password = input('Please enter password: \n')
print()
print('=' * 40)

if username not in data:
    print('No user found')
    exit()
elif data[username] != password:
    print('permission denied')
    exit()
else:
    print('permission allowed\n')
    print()
print('OUR TEXTS:')


text_1 = ('''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.''')


text_2 = ('''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''')

text_3 = ('''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.''')


your_choice = int(input('We have 3 texts to analyze, please choose 1, 2 or 3:\n'))
print()


if your_choice not in (1,2,3):
    print('No such text')
else:
    your_choice = int(your_choice)

print()

print('statistics:')
print()

if your_choice is 1:
    texts = text_1
    print(text_1)
elif your_choice is 2:
    texts = text_2
    print(text_2)
elif your_choice is 3:
    texts = text_3
    print(text_3)
else:
    print ('Invalid choice')

analyzing = texts
analyzing = analyzing.split()



#analyzing.split()

# capitals
capitals = 0
i = 0

while i < len(analyzing):
    if analyzing[i].istitle():
        capitals += 1
        i += 1
    else:
        i += 1

# uppercases

uppers = 0
i = 0

while i < len(analyzing):
    if analyzing[i].isupper() and not analyzing[i].isnumeric():
        uppers += 1
        i += 1
    else:
        i += 1

# lowercases

lowers = 0
i = 0

while i < len(analyzing):
    if analyzing[i].islower():
        lowers += 1
        i += 1
    else:
        i += 1

# numerics

numerics = 0
i = 0

while i < len(analyzing):
    if analyzing[i].isnumeric():
        numerics += 1
        i += 1
    else:
        i += 1

digits = analyzing.isnumeric()
digits = sum(str(digits))


print ('You text chosen text has ' + str(capitals) + ' capitals, ' + str(uppers) + ' uppercases, ' + str(lowers) + ' lowercases, ' + str(numerics) + ' numbers' + 'sum of digits is ' + int(digits))

print()
print('=' * 40)
print()

print('1' + ' - ' + str(capitals) + capitals * ' *' )
print('2' + ' - ' + str(uppers) + uppers * ' *' )
print('3' + ' - ' + str(lowers) + lowers * ' *' )
print('4' + ' - ' + str(numerics) + numberics * ' *' )

