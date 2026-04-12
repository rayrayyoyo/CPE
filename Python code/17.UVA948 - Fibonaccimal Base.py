import sys
fib = [1, 2]
while fib[-1] < 100000000:
    fib.append(fib[-1] + fib[-2])
input_data = sys.stdin.read().split()
if not input_data:
    sys.exit()
N = int(input_data[0])
queries = [int(x) for x in input_data[1 : N + 1]]
for q in queries:
    temp = q
    res = ""
    started = False 
    for f in reversed(fib):
        if temp >= f:
            res += "1"      
            temp -= f       
            started = True 
        elif started:
            res += "0"  
    print(f"{q} = {res} (fib)")