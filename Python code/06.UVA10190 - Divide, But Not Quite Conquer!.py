import sys

for line in sys.stdin:
    n, m = map(int, line.split())
    if n < 2 or m < 2:
        print("Boring!")
        continue
    ans = [n]
    while n > 1:
        if n % m == 0:
            n //= m
            ans.append(n)
        else:
            break
    if ans[-1] == 1:
        print(" ".join(map(str, ans)))
    else:
        print("Boring!")