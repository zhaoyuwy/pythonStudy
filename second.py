import first

# for i in range(10):
#     first.laugh()

for line in open('test.txt'):
    print(line)

f = open("test.txt")
print(f.name)
print(f.__next__())


def gen():
    a = 100
    yield a
    a = a * 8
    yield a
    yield 1000


for i in gen():
    print(i)

print(gen().__next__())
try:
    print(reduce((lambda x, y: x + y), [1, 2, 5, 7, 9]))
except NameError:
    print("name error")
print("######################")
a = 5
print(a)
b = a
print(b)
a = a + 2
print(a)
print(b)
print("DDDDDDDDDDDDDDD")
L1 = [1,2,3]
print(L1)
L2 = L1
L1[0] =10
print(L1)
print(L2)
print("#############")
def f2(x):
    x[0] = 2*3
    print (x)

a = [1,2,3]
f2(a)
print (a)
