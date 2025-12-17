# -*- coding: utf-8 -*-
import sys

# 一次讀取所有內容，處理可能的換行問題
input_data = sys.stdin.read().split()
iterator = iter(input_data)

try:
    while True:
        x = int(next(iterator))
        
        # 接下來讀取係數，這部分比較麻煩因為不知道有多少個
        # 這題通常是一行 x，下一行係數。
        # 因為我們用了 split() 把所有東西串在一起，沒辦法直接判斷換行。
        # 修正策略：改回逐行讀取比較安全
        pass
except StopIteration:
    pass

# 上面的 split 方法對這題不適用，因為需要靠換行來區分係數結尾
# 改用以下寫法：

def solve():
    lines = sys.stdin.readlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
            
        try:
            x = int(line)
            i += 1
            if i >= len(lines): break
            
            coeffs_str = lines[i].strip()
            # 有時候會有空行
            while not coeffs_str:
                i += 1
                if i >= len(lines): return
                coeffs_str = lines[i].strip()
                
            a = list(map(int, coeffs_str.split()))
            i += 1
            
            # Horner's Rule for Derivative
            # p(x) = a0*x^n + ... + an
            # p'(x) 計算
            n = len(a) - 1
            val = 0
            # 係數 a[0] 對應 x^n，微分後變成 n * a[0] * x^(n-1)
            # 最後一項常數微分為 0，所以 loop 到 n-1 (也就是倒數第二項)
            for j in range(n):
                val = val * x + a[j] * (n - j)
                
            print(val)
            
        except ValueError:
            i += 1

solve()