import sys

def solve(n):
    units = [ (10000000, "kuti"), (100000, "lakh"), (1000, "hajar"), (100, "shata") ]
    
    for val, name in units:
        if n >= val:
            solve(n // val)
            print(f" {name}", end="")
            n %= val
            
    if n > 0 or not any(n >= v for v, _ in units):
        if n > 0: print(f" {n}", end="")

case_num = 1
for line in sys.stdin:
    line = line.strip()
    if not line: continue
    
    print(f"{case_num:>4}.", end="")
    num = int(line)
    
    if num == 0:
        print(" 0")
    else:
        solve(num)
        print()
    case_num += 1