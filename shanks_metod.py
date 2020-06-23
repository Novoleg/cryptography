import random

p = 263
a = 79
y = 122
m = 0
k = 0

while m * k < p:
    m = random.randint(1, 20)
    k = random.randint(1, 20)
print(m, k)


def first_row():
    list_first_row = []
    for i in range(m):
        first_number_shanks = ((a ** i) * y) % p
        list_first_row.append(first_number_shanks)
    print(list_first_row)
    return list_first_row


def second_row():
    list_second_row = []
    for i in range(1, k + 1):
        second_number_shanks = (a ** (i * m)) % p
        list_second_row.append(second_number_shanks)
    print(list_second_row)
    return list_second_row


result_first_row = first_row()
result_second_row = second_row()

for i in range(len(result_first_row)):
    for j in range(len(result_second_row)):
        if result_first_row[i] == result_second_row[j]:
            index_firs_row = i
            index_second_row = j + 1
            print('Success!', result_first_row[i], 'Index of first row: ', index_firs_row, 'Index of second row: ',
                  index_second_row)
            x = index_second_row * m - index_firs_row
            print(x)

if (a ** x) % p == y:
    print('Решение найдено!')

