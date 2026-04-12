# -*- coding: utf-8 -*-
import sys

for line in sys.stdin:
    a, b = map(int, line.split())
    if a == 0 and b == 0: break # 看到 0 0 就收工
    count = 0  # 紀錄總共進位幾次
    carry = 0  # 紀錄目前的進位 (0 或 1)
    # 只要還有數字或還有進位沒處理完，就繼續跑
    while a > 0 or b > 0:
        # 當前位數相加 + 上次的進位
        val = (a % 10) + (b % 10) + carry
        
        if val >= 10:
            count += 1
            carry = 1  # 這次有進位，設定為 1 給下一輪用
        else:
            carry = 0  # 這次沒進位，歸零
            
        a //= 10 # 砍掉最後一位
        b //= 10 # 砍掉最後一位
        
    # 判斷輸出的英文格式
    if count == 0:
        print("No carry operation.")
    elif count == 1:
        print("1 carry operation.")
    else:
        print(f"{count} carry operations.")