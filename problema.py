n = int(input())

for i in range(n):
    a,b,c = [int(s) for s in input().split()]
    print(a ^ b  ^ c)