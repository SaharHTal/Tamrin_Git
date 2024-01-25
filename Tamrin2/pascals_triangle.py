def pascals_triangle(x):
    triangle =[]
    for i in range(x):
        row = [1] * (i + 1)
        triangle.append(row)
    for j in range (2, x):
        for k in range(1, j):
            triangle[j][k] = triangle[j - 1][k - 1] + triangle[j - 1][k]
    return triangle
def print_triangle(pascals_triangle):
    for rowline in pascals_triangle:
        for number in rowline:
            print(number, end=' ')
        print("")

x = int(input())
wanted_triangle = pascals_triangle(x)
print_triangle(wanted_triangle)