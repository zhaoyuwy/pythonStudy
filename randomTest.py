import math
import random

y = range(1, 23)
sample = random.sample(y, 5)
print(sample)

sum = 0
for i in range(8):
    integer = random.randint(1, 6)
    sum += integer * math.pow(10, i)

print(sum)
