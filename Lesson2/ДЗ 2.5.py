b = int(input())
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in a:
    if i == b:
        c = i
        a.insert(b, c)
    print(a)
    break