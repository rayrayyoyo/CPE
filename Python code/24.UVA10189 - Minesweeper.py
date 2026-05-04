import sys
data = sys.stdin.read().split()
idx = 0      
case_num = 1 

while idx < len(data):
    n = int(data[idx])
    m = int(data[idx+1])
    idx += 2  
    if n == 0 and m == 0:
        break    
    if case_num > 1:
        print()
    grid = []
    for _ in range(n):
        grid.append(list(data[idx]))
        idx += 1 
    print(f"Field #{case_num}:")
    for r in range(n):
        for c in range(m):
            if grid[r][c] == '*':
                print('*', end='')
            else:
                count = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == '*':
                            count += 1
                print(count, end='')
        print() 
        
    case_num += 1