# -*- coding: utf-8 -*-
import sys

def get_sum(s):
    return sum(int(c) for c in s)

for line in sys.stdin:
    s = line.strip()
    if s == "0":
        break
    
    # 先檢查第一層
    curr_sum = get_sum(s)
    
    if curr_sum % 9 != 0:
        print(f"{s} is not a multiple of 9.")
    else:
        degree = 1
        # 如果原本數字就是 9 的倍數且不是 '9' 本身，開始計算深度
        temp_n = curr_sum
        while temp_n > 9:
            temp_n = get_sum(str(temp_n))
            degree += 1
        
        # 特例：如果輸入就是 "9"，degree 應該是 1
        if s == "9": degree = 1
            
        print(f"{s} is a multiple of 9 and has 9-degree {degree}.")