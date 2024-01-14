# []
# newlist = [<transformer_expression> for <varname> in <sequence>]
# for filtering the sequence is conditionated with the same item.
def keep_evens(nums):
    new_list = [num for num in nums if num % 2 == 0]
    return new_list

print(keep_evens([3, 4, 6, 7, 0, 1]))


#EQUIVALENT:
things = [3, 4, 6, 7, 0, 1]
#chaining together filter and map:
# first, filter to keep only the even numbers
# double each of them
print(map(lambda x: x*2, filter(lambda y: y % 2 == 0, things)))

# equivalent version using list comprehension
print([x*2 for x in things if x % 2 == 0])


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
import json
tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}

js = json.dumps(tester, indent=2)
print(js)

jeje = tester['info']
a = []
for item in jeje:
    for i in item:
        if i == 'name':
            a.append(item[i])
#####################################################################
#ACTUAL WAY WITH LISTS COMPREHENSION
import json
tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}
print(json.dumps(tester, indent=2))
inner_list = tester['info']
compri = [d['name'] for d in inner_list]
print(compri)
#####################################################################
#FILTRATION EXPRESSIONS WITH LISTS
def longlenghts(strings): #LC
    return [len(s) for s in strings if len(s)>=4]
def longlenghts(strings):
    accum = []
    for s in strings:#NORMAL
        if len(s) >= 4:
            return(accum.append(s))
def longlenghts(strings):
    filtered_strings = filter(lambda s: len(s)>=4, strings)
    return(filtered_strings)
print(longlenghts(['a', 'bc', 'def', 'ghij', 'klmno']))
######################################################################
######################################################################
#ZIP
#Tuples the values of two list into one:
#[(1,2), (3,4), (5,6)

#1) NORMAL:
L1 = [3,4,5]
L2 = [1,2,3]
L3 = []
for i in range(len(L1)):
    L3.append(L1[i] + L2[i])
print(L3)
#2) ZIP:
L1 = [3,4,5]
L2 = [1,2,3]
L4 = list(zip(L1,L2))
for (x1,x2) in L4:
    L3.append(x1+x2)
print(L3)
#3) ZIP list comprehensions
L1 = [3,4,5]
L2 = [1,2,3]
L3 = [x1+x2 for (x1, x2) in list(zip(L1,L2))]
print(L3)
#4) map:
L1 = [3, 4, 5]
L2 = [1, 2, 3]
L3 = map(lambda x: x[0] + x[1], zip(L1, L2))
print(L3)


