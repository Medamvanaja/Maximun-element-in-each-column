m = int(input())
n = int(input())
a = []
for i in range(m):
    row = list(map(int, input().strip().split()))
    a.append(row)
for i in range(n):
    max = 0
    for j in range(m):
        if a[j][i] > max:
            max = a[j][i]
    print(max)
