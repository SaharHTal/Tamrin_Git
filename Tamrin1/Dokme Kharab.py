from operator import xor, and_, or_
a = int(input())
b = int(input())
k = int(input())
while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
if a == k:
    print(a)
    print("YES")
else:
    print(a)
    print("NO")