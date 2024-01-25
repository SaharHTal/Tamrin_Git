al = int(input())
ah = int(input())
n = int(input())
l = [int(input()) for i in range(n)]

a = format(ah, '032b') + format(al, '032b')
a = a[::-1]
for idx in l:
    if a[idx] == '1':
        print("yes")
    else:
        print("no")