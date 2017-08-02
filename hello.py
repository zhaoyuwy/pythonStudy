# #!/usr/bin/env python
# print('Hello world!')
#
#
# def func(a, b, c):
#     print(a, b, c)
#
#
# args = (1, 3, 4)
# func(*args)
#
# dict = {'a': 1, 'b': 2, 'c': 3}
# func(*dict)
#
# S = 'abcdefghijk'
# for (index, char) in enumerate(S):
#     print(index)
#     print(char)
# print("this LLLLLLLLLLLLLL")
# for i in range(0,len(S),2):
#     print (S[i])
#
#
# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# ta = [1,2,3]
# tb = [9,8,7]
# tc = ['a','b','c']
# print(zip(ta,tb,tc))
# for (a,b,c) in zip(ta,tb,tc):
#     print(a,b,c)

# print("###############################")
# ta = [1, 2, 3]
# tb = [9, 8, 7]
#
# # cluster
# zipped = zip(ta, tb)
# print(zipped)
#
# # decompose
# na, nb, nc = zip(*zipped)
# print(na, nb, nc)
#
# (-1).__abs__()

class VOW(object):
    def __init__(self, text):
        self.text = text
    def __enter__(self):
        self.text = "I say: " + self.text    # add prefix
        return self                          # note: return an object
    def __exit__(self,exc_type,exc_value,traceback):
        self.text = self.text + "!"          # add suffix


with VOW("I'm fine") as myvow:
    print(myvow.text)

print(myvow.text)


class bird(object):
    feather = True

class chicken(bird):
    fly = False
    def __init__(self, age):
        self.age = age

summer = chicken(2)

print(bird.__dict__)
print(chicken.__dict__)
print(summer.__dict__)

print("################")
def line_conf():
    def line(x):
        return 2*x+1
    print(line(5))   # within the scope


line_conf()
print(line_conf())       # out of the scope


print("###############")
# get square sum
def square_sum(a, b):
    return a**2 + b**2

# get square diff
def square_diff(a, b):
    return a**2 - b**2


print(square_sum(3, 4))
print(square_diff(3, 4))

print("#####################")
# modify: print input

# get square sum
def square_sum(a, b):
    print("intput:", a, b)
    return a**2 + b**2

# get square diff
def square_diff(a, b):
    print("input", a, b)
    return a**2 - b**2


print(square_sum(3, 4))
print(square_diff(3, 4))

print("################")
def decorator(F):
    def new_F(a, b):
        print("input", a, b)
        return F(a, b)
    return new_F

# get square sum
@decorator
def square_sum(a, b):
    return a**2 + b**2

# get square diff
@decorator
def square_diff(a, b):
    return a**2 - b**2

print(square_sum(3, 4))
print(square_diff(3, 4))