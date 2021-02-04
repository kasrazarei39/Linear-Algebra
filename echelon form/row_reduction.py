import numpy

print('Enter number of rows and columns respectively:')
row, column = [int(x) for x in input().split()]
inputs = numpy.zeros([row, column])
for i in range(row):
    print('Enter row', i + 1, ':')
    inputs[i] = [int(x) for x in input().split()]
print('Enter constant values:')
values = numpy.array([int(x) for x in input().split()]).reshape(row, 1)
arr = numpy.hstack((inputs, values))  # create Augmented matrix
print(arr, '\n')

ans = list()  # save base variable
pivot = 0
for j in range(column):
    for i in range(pivot, row):
        if arr[i][j] != 0:
            ans.append(j)
            arr[[pivot, i]] = arr[[i, pivot]]
            coefficient = arr[pivot][j]  # use for conversion the pivot to 1
            for t in range(column + 1):
                arr[pivot][t] = arr[pivot][t] / coefficient  # conversion the pivot to 1
            for k in range(pivot + 1, row):
                if arr[k][j] != 0:
                    tmp = -1 * arr[k][j]
                    for l in range(column + 1):
                        arr[k][l] = arr[pivot][l] * tmp + arr[k][l]  # conversion the numbers below pivot to 0
            for k in range(pivot - 1, -1, -1):
                if arr[k][j] != 0:
                    tmp = -1 * arr[k][j]
                    for l in range(column + 1):
                        arr[k][l] = arr[pivot][l] * tmp + arr[k][l]  # conversion the numbers above pivot to 0
            pivot += 1
            break

print(arr, '\n')

# check for exists answer
flg = False
for i in range(row):
    find = True
    for j in range(column):
        if arr[i][j] != 0:
            find = False
    if find:
        if arr[i][column] != 0:
            flg = True

if flg:
    print('Doesn\'t have answer')
else:
    cnt = 0
    for i in range(column):
        if i in ans:
            print(f'x{i + 1}:', end='')
            for k in range(ans[cnt] + 1, column):
                if arr[cnt][k] == 0:
                    continue
                print('(', - 1 * arr[cnt][k], f'x{k + 1}', ')', '+ ', end='')
            print('(', arr[cnt][column], ')')
            cnt += 1
        else:
            print(f'x{i + 1} is free')
