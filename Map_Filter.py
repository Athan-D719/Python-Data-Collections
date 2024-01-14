#EXE BEFORE MAPPING
def doubleStuff(a_list):
    """ Return a new list in which contains doubles of the elements in a_list. """
    new_list = []
    for value in a_list:
        new_elem = 2 * value
        new_list.append(new_elem)
    return new_list

things = [2, 5, 9]
print(things)
things = doubleStuff(things)
print(things)
'''
map(fun, iter)
    -fun = Function to which map passes each element of given iterable.
    -iter = iterable which is to be mapped.(ex.list)
'''
#MAPPING
def triple(value):
    return 3*value

def tripleStuff(a_list):
    new_seq = map(triple, a_list) #(fun, iter)
    return list(new_seq)

def quadrupleStuff(a_list):
    new_seq = map(lambda value: 4*value, a_list) #lambda iterate
    return list(new_seq)

things = [2, 5, 9]
things3 = tripleStuff(things)
print(things3)
things4 = quadrupleStuff(things)
print(things4)
##################################################################
##################################################################
#EXE BEFORE filtering
def keep_evens(nums):
    new_list = []
    for num in nums:
        if num % 2 == 0:
            new_list.append(num)
    return new_list

print(keep_evens([3, 4, 6, 7, 0, 1]))
'''
filter(function, sequence)
    -function: function that tests if each element of a 
               sequence true or not.
    -sequence: sequence which needs to be filtered, it can 
               be sets, lists, tuples, or containers of any iterators.
    -returns: returns an iterator that is already filtered.
    (returns booleans with the values to be filtered IN and OUT.)
'''
#FILTERING
def keep_evens(nums):
    new_seq = filter(lambda num: num % 2 == 0, nums)
    return list(new_seq)

print(keep_evens([3, 4, 6, 7, 0, 1]))




