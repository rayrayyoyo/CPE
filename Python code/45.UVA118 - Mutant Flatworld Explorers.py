# -*- coding: utf-8 -*-
import sys

def solve():
    input_data = sys.stdin.read().split()
    iterator = iter(input_data)
    
    try:
        # 讀取邊界
        max_x = int(next(iterator))
        max_y = int(next(iterator))
        
        # 紀錄掉落點 (Scents)
        scents = set()
        
        # 方向對應向量
        dirs = ['N', 'E', 'S', 'W']
        moves = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
        
        while True:
            try:
                x = int(next(iterator))
                y = int(next(iterator))
                d_char = next(iterator)
                d_idx = dirs.index(d_char)
                
                cmds = next(iterator)
                
                lost = False
                for cmd in cmds:
                    if cmd == 'R':
                        d_idx = (d_idx + 1) % 4
                    elif cmd == 'L':
                        d_idx = (d_idx - 1 + 4) % 4
                    elif cmd == 'F':
                        curr_dir = dirs[d_idx]
                        dx, dy = moves[curr_dir]
                        nx, ny = x + dx, y + dy
                        
                        # 檢查邊界
                        if nx < 0 or nx > max_x or ny < 0 or ny > max_y:
                            # 機器人要掉下去了
                            if (x, y) in scents:
                                # 有前人留下的味道，忽略指令
                                continue
                            else:
                                # 真的掉下去了
                                lost = True
                                scents.add((x, y))
                                break
                        else:
                            x, y = nx, ny
                            
                result = f"{x} {y} {dirs[d_idx]}"
                if lost:
                    result += " LOST"
                print(result)
                
            except StopIteration:
                break
                
    except StopIteration:
        pass

solve()