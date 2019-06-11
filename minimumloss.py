n=int(input())

l = [int(item) for item in input().split()]
l2 = l.copy()
d={}
for i in range(len(l)):
    d[l[i]] = i
l = sorted(l)
m = float("inf")
for i in range(len(l)-1):
    if d[l[i+1]] < d[l[i]] : m = min(m,l[i + 1] - l[i])
print(m)