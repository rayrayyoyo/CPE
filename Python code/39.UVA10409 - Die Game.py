# -*- coding: utf-8 -*-
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data: return
    iterator = iter(input_data)
    
    try:
        while True:
            try:
                k = int(next(iterator))
            except StopIteration:
                break
                
            if k == 0: break
            
            # 1=Top, 2=North, 3=West (題目預設)
            # 因為骰子對面和為 7，所以 South=7-North, East=7-West, Bottom=7-Top
            t, n, w = 1, 2, 3
            
            for _ in range(k):
                cmd = next(iterator)
                if cmd == 'north':
                    t, n = 7-n, t
                elif cmd == 'south':
                    t, n = n, 7-t
                elif cmd == 'east':
                    # 向東滾：原本的西面(w)變成頂面(t)，原本的頂面(t)變成東面(7-w)
                    t, w = w, 7-t
                elif cmd == 'west':
                    # 向西滾：原本的東面(7-w)變成頂面(t)，原本的頂面(t)變成西面(w)
                    t, w = 7-w, t
            print(t)
    except StopIteration:
        pass

if __name__ == '__main__':
    solve()