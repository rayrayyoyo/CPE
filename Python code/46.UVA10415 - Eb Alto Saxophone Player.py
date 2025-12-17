# -*- coding: utf-8 -*-
import sys

# 簡化映射表，用字串處理即可
fingers = {
    'c': [2,3,4,7,8,9,10], 'd': [2,3,4,7,8,9], 'e': [2,3,4,7,8],
    'f': [2,3,4,7], 'g': [2,3,4], 'a': [2,3], 'b': [2],
    'C': [3], 'D': [1,2,3,4,7,8,9], 'E': [1,2,3,4,7,8],
    'F': [1,2,3,4,7], 'G': [1,2,3,4], 'A': [1,2,3], 'B': [1,2]
}

def solve():
    # 讀取所有行
    lines = sys.stdin.readlines()
    if not lines: return
    
    try:
        t_str = lines[0].strip()
        if not t_str: return
        T = int(t_str)
        
        for i in range(1, T + 1):
            if i >= len(lines): break
            notes = lines[i].strip() # 讀取音符字串
            
            # 手指按下次數統計 (index 1-10)
            press_counts = [0] * 11
            # 當前手指狀態 (True 為按住)
            current_state = [False] * 11
            
            for note in notes:
                needed = fingers.get(note, [])
                next_state = [False] * 11
                
                # 標記下一階段需要按的手指
                for finger in needed:
                    next_state[finger] = True
                    
                # 檢查變化：如果下一階段要按，且目前沒按 -> 增加計數
                for f in range(1, 11):
                    if next_state[f] and not current_state[f]:
                        press_counts[f] += 1
                
                current_state = next_state
                
            # 輸出 1-10 的次數
            print(*(press_counts[1:11]))
            
    except ValueError:
        pass

solve()