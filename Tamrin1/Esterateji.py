from math import sqrt, floor
def is_prime(num):
    if num < 2: return False
    if num == 2: return True
    if num % 2 == 0: return False
    for i in range(3,floor(sqrt(num))+1,2):
        if num % i == 0: return False
    return True
a, b = map(int, input().split())
c = 0
if a <= b:
    print('main order - amount: ', end='', sep='')
else:
    a,b = b,a
    print('reverse order - amount: ', end='', sep='')
for i in range(a,b+1):
    if is_prime(i):
        c += 1
print(c, sep='')