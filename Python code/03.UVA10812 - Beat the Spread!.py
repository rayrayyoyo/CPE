case = int(input())
for i in range(case):
    s, d = map(int, input().split())
    if s < d or (s + d) % 2 == 1:
        print("impossible")
    else:
        print((s + d) // 2, (s - d) // 2)