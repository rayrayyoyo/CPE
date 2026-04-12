import sys
def f(n):
    if n % 2 != 0:
        return n * 3 + 1
    else:
        return n // 2
for line in sys.stdin: 
    i, j = map(int, line.split())
    min1 = min(i, j)
    max1 = max(i, j)
    max_cycle = 0
    for k in range(min1, max1 + 1):
        l = 1
        curr = k
        while curr != 1:
            curr = f(curr)
            l += 1
        
        if l > max_cycle:
            max_cycle = l

    print(i, j, max_cycle)