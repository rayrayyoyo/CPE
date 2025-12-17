# -*- coding: utf-8 -*-
import sys

# 這題的重點在於 Python 3 的 sort key 怎麼寫
# 比較邏輯：
# 1. 餘數 (mod M) 由小到大
# 2. 若餘數相等：
#    a. 奇數優先於偶數
#    b. 若都是奇數，大於小 (降序)
#    c. 若都是偶數，小於大 (升序)

def solve():
    input_data = sys.stdin.read().split()
    iterator = iter(input_data)
    
    try:
        while True:
            N = int(next(iterator))
            M = int(next(iterator))
            
            print(f"{N} {M}")
            if N == 0 and M == 0:
                break
                
            nums = []
            for _ in range(N):
                nums.append(int(next(iterator)))
                
            # 定義排序 Key
            def sort_key(n):
                # 1. 餘數
                remainder = n % M
                
                # 2. 奇偶性 (0 為奇, 1 為偶，讓奇數排前面)
                # 注意：Python 的負數取餘數行為可能與 C++ 不同
                # 例如 -3 % 2 = 1，這點沒問題
                is_even = 1 if n % 2 == 0 else 0
                
                # 3. 數值本身的排序方向
                # 如果是奇數，要降序 -> 取負值 (-n)
                # 如果是偶數，要升序 -> 取正值 (n)
                val_order = n if is_even else -n
                
                return (remainder, is_even, val_order)
                
            nums.sort(key=sort_key)
            
            for n in nums:
                print(n)
                
    except StopIteration:
        pass

solve()