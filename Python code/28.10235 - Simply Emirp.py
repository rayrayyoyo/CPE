# -*- coding: utf-8 -*-
import sys

def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    # 優化：只檢查到開根號即可
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
        
    try:
        n = int(line)
        # 1. 檢查是否為質數
        if not is_prime(n):
            print(f"{n} is not prime.")
        else:
            # 2. 檢查反轉後是否不一樣且為質數
            rev_s = str(n)[::-1]
            rev_n = int(rev_s)
            
            if rev_n != n and is_prime(rev_n):
                print(f"{n} is emirp.")
            else:
                print(f"{n} is prime.")
    except ValueError:
        break