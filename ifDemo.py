# i = 1
# x = 1
# if i > 0:
#     x = x+1
# print (x)
#
#
# def square_sum(a,b):
#     c = a*2 + b**2
#     print(a*2)
#     return c
#
#
# print(square_sum(3,4))
#
#
#
#
# a = 1
#
# def change_integer(a):
#     a = a + 1
#     return a
#
# print (change_integer(a))
# print (a)
#
# #===(Python中 "#" 后面跟的内容是注释，不执行 )
#
# b = [1,2,3]
#
# def change_list(b):
#     b[0] = b[0] + 1
#     return b
#
# print (change_list(b))
# print (b)



class Bird():
    have_feather = True
    way_of_reproduction = 'egg'

    def move(self, dx, dy):
        position = [0, 0]
        position[0] = position[0] + dx
        position[1] = position[1] + dy
        return position


summer = Bird()
print('after move:', summer.move(5, 8))


class Chicken(Bird):
    way_of_move = 'walk'
    possible_in_KFC = True


class Oriole(Bird):
    way_of_move = 'fly'
    possible_in_KFC = False


summer = Chicken()
print(summer.have_feather)
print(summer.move(5, 8))


class Human(object):
    laugh = 'hahahaha'

    def show_laugh(self):
        print(self.laugh)

    def laugh_100th(self):
        for i in range(10):
            self.show_laugh()


li_lei = Human()
li_lei.laugh_100th()


class happyBird(Bird):
    def __init__(self, more_words):
        print('We are happy birds.', more_words)


summer = happyBird('Happy,Happy!')


class superList(list):
    def __sub__(self, b):
        a = self[:]  # 这里，self是supeList的对象。由于superList继承于list，它可以利用和list[:]相同的引用方法来表示整个对象。
        b = b[:]
        while len(b) > 0:
            element_b = b.pop()
            if element_b in a:
                a.remove(element_b)
        return a


print(type(superList([1, 2, 3])))
print(superList([1, 2, 3]))
print(superList([1, 2, 3]) - superList([3, 4]))
# print(list([1, 2, 3]) - list([3, 4]))


dic = {'tom': 11, 'sam': 57, 'lily': 100}
dic = {}
print(dic)
print(type(dic))

dic = {'lilei': 90, 'lily': 100, 'sam': 57, 'tom': 90}
for key in dic:
    print(dic[key])


def f(a, b, c):
    return a + b + c


print(f(1, 2, 3))
print(f(c=3, b=2, a=1))
print(f(1, c=3, b=2))


# def f(a, b, c=10):
#     return a + b + c


# print(f(3, 2))
print(f(3, 2, 1))


def func(*name):
    print (type(name))
    print (name)

# func(1,4,6)
# func(5,6,7,1,2,3)
func(a=1,b=9)
func(m=2,n=1,c=11)