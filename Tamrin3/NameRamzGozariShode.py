message = []
position = [0]
max_character = max(position)

codes = input().split()
for code in codes:
    position.append((int(code[1:]))+1)
    max_character = max(position)

i=-1
while i < max_character:
    i += 1
    for code in codes:
        if i == 0:
            if len(code) == 2:
                if str(i) in code[1:]:
                    message.append(code[0])
        elif (10**(len(code)-2)) <= i < (10**(len(code)-1)):
            if str(i) in code[1:]:
                message.append(code[0])


for letter in message:
    print(letter, end="")
