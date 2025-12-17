# -*- coding: utf-8 -*-
import sys

# 一次讀兩行
lines = sys.stdin.readlines()

for i in range(0, len(lines), 2):
    if i + 1 >= len(lines): break # 防止最後一行落單
    
    a = lines[i].strip()
    b = lines[i+1].strip()
    
    # 計數 a 和 b 裡面的字母
    # 只要檢查 a 到 z
    result = []
    for char_code in range(ord('a'), ord('z') + 1):
        char = chr(char_code)
        count_a = a.count(char)
        count_b = b.count(char)
        
        # 取兩邊出現次數的最小值
        common_count = min(count_a, count_b)
        result.append(char * common_count)
        
    print("".join(result))