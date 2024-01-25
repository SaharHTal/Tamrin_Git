a = int(input())
b = int(input())
c = bin(a ^ b)
print(len(c.replace("b","" ).replace("0","")))
