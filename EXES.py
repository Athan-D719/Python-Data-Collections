#1) extracting US medals.
nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}

US_count = []
for con in nested_d:
    for fl in nested_d[con]:
        if fl == 'USA':
            US_count.append(nested_d[con][fl])
print(US_count)

#2) map, lambda

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
def dbl(li):
    return li*2
greeting_doubled = map(lambda val : val*2, lst)
print(greeting_doubled)

#################################################


abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]
def up(lst):
    return lst.upper()

abbrevs_upper = map(up, abbrevs)
print(abbrevs_upper)

#3)filtering lambda ""

lst = ["witch", "halloween", "pumpkin", "cat", "candy", "wagon", "moon"]
lst2 = filter(lambda word: "o" in word, lst)
print(lst2)
####################################################################
#HANG GAME:
def possible(word, blanked, guesses_made):
    if len(word) != len(blanked):
        return False
    for i in range(len(word)):
        bc = blanked[i]
        wc = word[i]
        if bc == '_' and wc in guesses_made:
            return False
        elif bc != '_' and bc != wc:
            return False
    return True

print(possible("wonderwall", "_on__r__ll", "otnqurl"))
print(possible("wonderwall", "_on__r__ll", "wotnqurl"))
####################################################
#WITH ZIP
def possible(word, blanked, guesses_made):
    if len(word) != len(blanked):
        return False
    for (bc, wc) in zip(blanked, word):
        if bc == '_' and wc in guesses_made:
            return False
        elif bc != '_' and bc != wc:
            return False
    return True

print(possible("wonderwall", "_on__r__ll", "otnqurl"))
print(possible("wonderwall", "_on__r__ll", "wotnqurl"))
    
################################################################
#Extracting the second name.
people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]
first_names = [d[1] for d in people]
print(first_names)
################################################################
#s[0], s[1]
students = [('Tommy', 95), ('Linda', 63), ('Carl', 70), ('Bob', 100), ('Raymond', 50), ('Sue', 75)]
passed = [s[0] for s in students if s[1] >= 70 ]
print(passed)
################################################################
#len, zip, filter
l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
opposites = filter(lambda x: len(x[0])>3 and  len(x[1]) , list(zip(l1, l2)))
###################################################################
athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'], ['Felix', 'Bolt', 'Gardner', 'Eaton'], ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]
t =[]
other = []

for i in athletes:
    t += ([x for x in i if "t" in x])
    other += ([x for x in i if "t" not in x])
################################################################
info = [['Tina', 'Turner', 1939, 'singer'], ['Matt', 'Damon', 1970, 'actor'], ['Kristen', 'Wiig', 1973, 'comedian'], ['Michael', 'Phelps', 1985, 'swimmer'], ['Barack', 'Obama', 1961, 'president']]

last_names = [x[1] for x in info ]
#################################################################
nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}
for i in nested_d:
    if i == 'London':
        london_gold = [nested_d[i][x] for x in nested_d[i] if x == 'Great Britain']
##############################################################################################
nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}
US_count = []
for i in nested_d:
    US_count += [nested_d[i][x] for x in nested_d[i] if x == 'USA'] 
##############################################################################################
           
