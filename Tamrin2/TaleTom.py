def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def lcm(x, y):
    return (x * y) // gcd(x, y)
def lcd(nums):
    lcd = 1
    for num in nums:
        lcd = lcm(lcd, int(num))
    return lcd
def gcd_list(nums):
    gcd_list = nums[0]
    for num in nums:
        gcd_list = gcd(gcd_list, int(num))
    return gcd_list
command = input()
def farar(command):
    if command == "sum":
        numbers = []
        while True:
            value = input()
            if value == 'end':
                print(sum(numbers))
                break
            numbers.append(int(value))
    elif command == "average":
        numbers = []
        while True:
            value = input()
            if value == "end":
                print(round(sum(numbers) / len(numbers), 2))
                break
            numbers.append(int(value))
    elif command == "lcd":
        numbers = []
        while True:
            value = input()
            if value == "end":
                print(lcd(numbers))
                break
            numbers.append(int(value))
    elif command == "gcd":
        numbers = []
        while True:
            value = input()
            if value == "end":
                print(gcd_list(numbers))
                break
            numbers.append(int(value))
    elif command == "min":
        numbers = []
        while True:
            value = input()
            if value == "end":
                print(min(numbers))
                break
            numbers.append(int(value))
    elif command == "max":
        numbers = []
        while True:
            value = input()
            if value == "end":
                print(max(numbers))
                break
            numbers.append(int(value))
    else:
        print("Invalid command")
farar(command)
