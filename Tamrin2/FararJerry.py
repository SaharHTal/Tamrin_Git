def _map(n, moves):
    map_grid = [['.' for x in range(n)]]
    global position
    position = [0, 0]
    map_grid[0][0] = "*"
    for move in moves:
        if move == "R":
            position[1] += 1
        elif move == "L":
            position[1] -= 1
        elif move == "B":
            map_grid.append(['.' for x in range(n)])
            position[0] += 1
        global j
        i = position[0]
        j = position[1]
        if j <= -1:
            j +=1
            position[1] +=1
        if j > n-1:
            j -=1
            position[1] -=1
        map_grid[i][j] = '*'
    return map_grid
n = int(input())
moves = []
while True:
    move = input()
    if move == "END":
        break
    moves.append(move)
result_map = _map(n,moves)
if position[1] != n-1:
    for row in result_map:
        print(' '.join(row))
    print("There's no way out!")
else:
    for row in result_map:
        print(' '.join(row))