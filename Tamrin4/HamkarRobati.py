import numpy as np
f = open("filename.txt", "r")
n, m = map(int, f.readline().split())
list_of_arrays = []
for _ in range(n):
    tmp_array = np.array([])
    for j in range(m):
        tmp_array = np.concatenate((tmp_array, np.array(list(map(int, f.readline().split())))))
    list_of_arrays.append(tmp_array)
for i, x in enumerate(list_of_arrays):
    list_of_arrays[i] = list_of_arrays[i].reshape(m, m)
detofdotswithindex = []
detofdot = []
for i in range(len(list_of_arrays)):
    for j in range(i + 1, len(list_of_arrays)):
        detofdotswithindex.append((i, j, np.linalg.det(np.dot(list_of_arrays[i], list_of_arrays[j]))))
        detofdot.append(np.linalg.det(np.dot(list_of_arrays[i], list_of_arrays[j])))
for i1, j1, k1 in detofdotswithindex:
    if k1 == max(detofdot):
        i = i1
        j = j1
        break
if np.linalg.det(list_of_arrays[i]) > np.linalg.det(list_of_arrays[j]):
    result = np.linalg.inv(np.dot(list_of_arrays[i], list_of_arrays[j]))
elif np.linalg.det(list_of_arrays[i]) < np.linalg.det(list_of_arrays[j]):
    result =np.linalg.inv(np.dot(list_of_arrays[j], list_of_arrays[i]))
else:
    result = np.linalg.inv(np.dot(list_of_arrays[i], list_of_arrays[j]))
for _ in result:
    for x in _:
        print(f"{round(x, 3):.3f}", end=" ")
    print()

