import sys

for line in sys.stdin:
    n = line.strip()
    if n == '0':
        break
        
    while len(n) > 1:
        total = sum(int(c) for c in n)
        n = str(total)
        
    print(n)