# -*- coding: utf-8 -*-
import sys

for line in sys.stdin:
    parts = line.split()
    if len(parts) < 2:
        continue
        
    a_str = parts[0]
    b_str = parts[1]
    
    if a_str == '0' and b_str == '0':
        break
        
    # 補零讓長度一樣，方便從尾巴開始加
    max_len = max(len(a_str), len(b_str))
    a_str = a_str.zfill(max_len)
    b_str = b_str.zfill(max_len)
    
    carry = 0
    carry_count = 0
    
    # 從最後一位往回算
    for i in range(max_len - 1, -1, -1):
        val_a = int(a_str[i])
        val_b = int(b_str[i])
        
        if val_a + val_b + carry >= 10:
            carry = 1
            carry_count += 1
        else:
            carry = 0
            
    if carry_count == 0:
        print("No carry operation.")
    elif carry_count == 1:
        print("1 carry operation.")
    else:
        print(f"{carry_count} carry operations.")