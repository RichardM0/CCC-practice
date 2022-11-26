"""
3
AB GL JK
2
DF DG
4 ACG BDF EHI JKL
"""
mustt = []
musts = []
groups = []

x = int(input())
for i in range(x):
    a = input().split()
    mustt.append(a)

c1 = x
c2 = 0

y = int(input())
for i in range(y):
    b = input().split()
    musts.append(b)

g = int(input())
for i in range(g):
    c = input().split()
    groups.append(c)

for i in mustt:
    for j in groups:
        if "".join(i) in "".join(j):
            fin1 = all([x in i for x in j])
            if fin1:
                c1-=1

for i in mustt:
    for j in groups:
        if "".join(i) in "".join(j):
            fin1 = all([x in i for x in j])
            if fin1:
                c2+=1
print(mustt)
print(musts)
print(groups)
print(c2+c1)

