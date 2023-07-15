n = int(input("n="))
m = int(input("m="))
x = []
x1 = []
for i in range(n):
    x.append([])
    x1.append([])
    for j in range(m):
        x[i].append(int(input("sonlar")))
        x1[i].append(int(input("sonlar;")))
k = int(input("k"))
for e in range(k):
    for i in range(len(x)-1):
        for j in range(m-1):
            x1[i][m-1] = x[i+1][m-1]
            x1[n - 1][m - 1] = x[n - 1][m - 2]
            x1[n - 1][0] = x[n - 2][0]
            x1[i + 1][0] = x[i][0]
print(x1)