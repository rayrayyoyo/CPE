import sys
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue    
    n = int(line)
    if n == 0:
        break
    if n % 11 == 0:
        print(f"{line} is a multiple of 11.")
    else:
        print(f"{line} is not a multiple of 11.")