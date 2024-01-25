code_posti = list(map(int, input().split()))
jam = int(input())
sum_of_indices = {}
sum_of_indices2 = []
for i in range(len(code_posti)):
    complement = jam - code_posti[i]
    if complement in sum_of_indices:
        sum_of_indices2.append(sum_of_indices[complement] + i)
    sum_of_indices[code_posti[i]] = i
sum_of_indices2.sort()
for _ in sum_of_indices2:
    print(_)
if not sum_of_indices2:
    print("Not Found!")
