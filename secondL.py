arr = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

for i in range(len(arr)):
    count = 0
    if arr[i] < 0:
        count += 1
        print(count)    