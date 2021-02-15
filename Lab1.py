Taras Kalaida, [15 Feb 2021, 13:39:05]:
import random as rm

a0, a1, a2, a3, x_list, xn_list, y_list, x0_list, dx_list, max_y = 12, 8, 11, 5, [], [], [], [], [], 500
abc_list1 = ["№  X1  X2  X3   Y"]
abc_list2 = ["№  Xn1  Xn2  Xn3 "]
for i in range(8):
    x_list.append([])
    for j in range(3):
        x_list[i].append(float(rm.randint(0, 20)))

for i in range(8):
    y_list.append(a0 + x_list[i][0] * a1 + x_list[i][1] * a2 + x_list[i][2] * a3)

for i in range(3):
    new_list = []
    for j in range(8):
        new_list.append(x_list[j][i])
    x0 = (min(new_list) + max(new_list)) / 2
    x0_list.append(x0)
    dx_list.append(x0 - min(new_list))
average_y = sum(y_list) / 8
x0_y = a0 + a1 * x0_list[0] + a2 * x0_list[1] + a3 * x0_list[2]


for i in range(8):
    xn_list.append([])
    for j in range(3):
        xn_list[i].append(round((x_list[i][j] - x0_list[j]) / dx_list[j], 2))
for i in y_list:
    if i > average_y:
        if i<max_y:
            max_y = i
x0_list.append(x0_y)
dx_list.append(average_y)
print((str(abc_list1)[1:-1]).replace(",", ""))
for i in range(8):
    print(i + 1, (str(x_list[i])[1:-1]).replace(",", ''), y_list[i])
print("x0", (str(x0_list)[1:-1]).replace(",", ""), "\ndx", (str(dx_list)[1:-1]).replace(",", ""))
print("a0 - ", str(a0) + ",", "a1 - ", str(a1) + ",", "a2 - ", str(a2) + ",", "a3 - ", str(a3) + ",", "average Y - ",
      str(average_y) + ",", "average Y > - ", str(max_y) + ".")
print((str(abc_list2)[1:-1]).replace(",", ""))
for i in range(8):
    print(i + 1, (str(xn_list[i])[1:-1]).replace(",", ''))

`import random as rm

a0, a1, a2, a3, x_list, xn_list, y_list, x0_list, dx_list, max_y = 12, 8, 11, 5, [], [], [], [], [], 500
abc_list1 = ["№  X1  X2  X3   Y"]
abc_list2 = ["№  Xn1  Xn2  Xn3 "]
for i in range(8):
    x_list.append([])
    for j in range(3):
        x_list[i].append(float(rm.randint(0, 20)))

for i in range(8):
    y_list.append(a0 + x_list[i][0] * a1 + x_list[i][1] * a2 + x_list[i][2] * a3)

for i in range(3):
    new_list = []
    for j in range(8):
        new_list.append(x_list[j][i])
    x0 = (min(new_list) + max(new_list)) / 2
    x0_list.append(x0)
    dx_list.append(x0 - min(new_list))
average_y = sum(y_list) / 8
x0_y = a0 + a1 * x0_list[0] + a2 * x0_list[1] + a3 * x0_list[2]


for i in range(8):
    xn_list.append([])
    for j in range(3):
        xn_list[i].append(round((x_list[i][j] - x0_list[j]) / dx_list[j], 2))
for i in y_list:
    if i > average_y:
        if i<max_y:
            max_y = i
x0_list.append(x0_y)
dx_list.append(average_y)
print((str(abc_list1)[1:-1]).replace(",", ""))
for i in range(8):
    print(i + 1, (str(x_list[i])[1:-1]).replace(",", ''), y_list[i])
print("x0", (str(x0_list)[1:-1]).replace(",", ""), "\ndx", (str(dx_list)[1:-1]).replace(",", ""))
print("a0 - ", str(a0) + ",", "a1 - ", str(a1) + ",", "a2 - ", str(a2) + ",", "a3 - ", str(a3) + ",", "average Y - ",
      str(average_y) + ",", "average Y < - ", str(max_y) + ".")
print((str(abc_list2)[1:-1]).replace(",", ""))
for i in range(8):
    print(i + 1, (str(xn_list[i])[1:-1]).replace(",", ''))

import random as rm

a0, a1, a2, a3, x_list, xn_list, y_list, x0_list, dx_list, max_y = 12, 8, 11, 5, [], [], [], [], [], 500
abc_list1 = ["№  X1  X2  X3   Y"]
abc_list2 = ["№  Xn1  Xn2  Xn3 "]
for i in range(8):
    x_list.append([])
    for j in range(3):
        x_list[i].append(float(rm.randint(0, 20)))

for i in range(8):
    y_list.append(a0 + x_list[i][0] * a1 + x_list[i][1] * a2 + x_list[i][2] * a3)

for i in range(3):
    new_list = []
    for j in range(8):
        new_list.append(x_list[j][i])
    x0 = (min(new_list) + max(new_list)) / 2
    x0_list.append(x0)
    dx_list.append(x0 - min(new_list))
average_y = sum(y_list) / 8
x0_y = a0 + a1 * x0_list[0] + a2 * x0_list[1] + a3 * x0_list[2]


for i in range(8):
    xn_list.append([])
    for j in range(3):
        xn_list[i].append(round((x_list[i][j] - x0_list[j]) / dx_list[j], 2))
for i in y_list:
    if i > average_y:
        if i<max_y:
            max_y = i
x0_list.append(x0_y)
dx_list.append(average_y)
print((str(abc_list1)[1:-1]).replace(",", ""))
for i in range(8):
    print(i + 1, (str(x_list[i])[1:-1]).replace(",", ''), y_list[i])
print("x0", (str(x0_list)[1:-1]).replace(",", ""), "\ndx", (str(dx_list)[1:-1]).replace(",", ""))
print("a0 - ", str(a0) + ",", "a1 - ", str(a1) + ",", "a2 - ", str(a2) + ",", "a3 - ", str(a3) + ",", "average Y - ",
      str(average_y) + ",", "average Y < - ", str(max_y) + ".")
print((str(abc_list2)[1:-1]).replace(",", ""))
for i in range(8):
    print(i + 1, (str(xn_list[i])[1:-1]).replace(",", ''))
