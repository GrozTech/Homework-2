a = list(input('Заполните список '))
b = 0
for i in range(len(a) // 2):
    a[b], a[b + 1] = a[b + 1], a[b]
    b += 2
print(a)