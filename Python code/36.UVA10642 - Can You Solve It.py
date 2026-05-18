import sys

def get_pos(x, y):
    n = x + y
    return (n * (n + 1)) // 2 + x

input_data = sys.stdin.read().split()

if input_data:
    n_cases = int(input_data[0])
    idx = 1
    
    for i in range(1, n_cases + 1):
        x1, y1, x2, y2 = map(int, input_data[idx:idx+4])
        idx += 4
        
        diff = get_pos(x2, y2) - get_pos(x1, y1)
        print(f"Case {i}: {diff}")