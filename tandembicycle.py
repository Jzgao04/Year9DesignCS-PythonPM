Q = int(input())
N = int(input())
dmoj = sorted([int(a) for a in input().split()])
peg = sorted([int(a) for a in input().split()])
if Q == 2:
    dmoj = dmoj[::-1]
print(sum([max(x,n) for x,n in zip(dmoj,peg)]))