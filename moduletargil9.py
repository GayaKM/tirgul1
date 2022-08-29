#1
def len(rashima:list):
    """function Len without using len"""
    count=0
    for i in rashima:
        count += 1
    return count

#2
def count(rashima:list, num:int):
    """function count how many times the given number is in the given list"""
    count = 0
    for i in rashima:
        if i == num:
            count += 1
    return count

#3
def find(numlist:list, num:int, ind=0):
    """function find the first index the given number is in the given list"""
    for i in range(ind,len(numlist)+1):
        if num==numlist[i]:
            return i

#4
def max(rashima:list):
    """function max returns the max value in the given list"""
    max = rashima[0]
    for i in rashima:
        if i >= max:
            max = i
    return max

#5
def list(multiclass):
    """function list returns the given dict, str, tuple, set as a list"""
    newlist=[]
    if type(multiclass) == dict or type(multiclass) == set or type(multiclass) == str or type(multiclass) == tuple:
        for i in multiclass:
            newlist.append(i)
        return newlist
    else:
        print("it's an error")
        return None

#6
def remove(rashima: list, value):
    """function remove, removes the given value from the given list"""
    newlist=[]
    if value in rashima:
        for i in rashima:
            if i != value:
                newlist.append(i)
        rashima = newlist
    else:
        print("it's an error")

#7
def keys (sifria:dict):
    """function keys, makes a list of the keys and returns it"""
    newlist = []
    for key in sifria:
        newlist.append(key)
    return newlist

#8
def values (sifria:dict):
    """function values, makes a list of the values and returns it"""
    newlist = []
    for key in sifria:
        newlist.append(sifria[key])
    return newlist

#9
def items(sifria:dict):
    """function items, gets a dictionary and turns it into tuple and returns it"""
    newtuple = ()
    for key in sifria:
        newtuple += (key, sifria[key])
    return newtuple

#10
def set(rashima: list):
    """function items, gets a dictionary and turns it into tuple and returns it"""
    newset=set({})
    for i in rashima:
        newset.add(i)
    return newset

rasima =[ 1,2,3,4,5,6,7,8,9,1,4]
print(f"len: {len(rasima)}")
number = 1
print(f"count: {count(rasima,number)}")
ind = 2
number = 4
print(f"find: {find(rasima,number,ind)}")
print(f"max: {max(rasima)}")
sifria = {10: 1, 20: 2, 30: 3, 40: 4, 50: 5}
print(f"list: {list(sifria)}")
number = 2
remove(rasima, number)
print(f"remove: {rasima}")
print(f"keys: {keys(sifria)}")
print(f"values: {values(sifria)}")
print(f"items: {items(sifria)}")
print(f"set: {rasima}")
