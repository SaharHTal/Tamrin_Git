def sum_divisors(num):
    _sum = 0
    for i in range(1, num + 1):
        if num % i == 0:
            _sum += i
    return _sum
def num_to_base(num, base):
    if not 2<= base <= 9:
        return "invalid base!"
    else:
        result = ""
        while num > 0:
            remainder = num % base
            result = str(remainder) + result
            num = num // base
        return result
_list =[]
sum2 = 0
try:
    while True:
        num1 = list(map(int, input().split()))
        if num1 == [-1, -1]:
            for i in _list:
                sum2 +=int((num_to_base(sum_divisors(i[0]), i[1])))
            print(sum2)
            break
        else:
            _list.append(num1)
except ValueError:
    print("invalid base!")