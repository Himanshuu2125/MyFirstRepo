a = int(input())
if not 1<=a<=2*(10**5):
    exit()
b = input()

c = b.split()
d = []
for i in c:
    d.append(int(i))
for i in d:
    if not 1<=i<=10**15:
        exit()

e = []

for i in range(0,len(d)):
    if d[i] not in e:
        e.append(d[i])



f = []
for i in e:
    g = 0
    for j in d:
        if i == j:
            g+=1
    f.append(g)



g = max(f)
h = 0
for i in f:
    if i == g:
        h+=1
print(h)


