# -*- coding: utf-8 -*-
import sys
import math

for line in sys.stdin:
    if not line.strip():
        continue
    try:
        s, d = map(int, line.split())
        # 數學解法：
        # 我們要找一個天數 k (代表最後一組的人數是 k)，使得
        # 從 S 加到 k 的總和 >= D
        # 等差級數公式： (S + k) * (k - S + 1) / 2 >= D
        # 整理後得到一元二次方程式： k^2 + k + (S - S^2 - 2D) >= 0
        # 利用公式解求 k，取正根
        # 係數 a=1, b=1, c = S - S^2 - 2D
        c = s - s**2 - 2*d
        # k = (-1 + sqrt(1 - 4c)) / 2
        delta = 1 - 4*c
        k = (-1 + math.isqrt(delta)) / 2
        # 因為是整數除法可能有誤差，稍微檢查一下
        # 這裡 k 是近似值，我們確保算出來的 k 對應的總和 >= D
        # 如果不夠，就往上加 1 (雖然公式解通常精準)
        # 直接用浮點數算比較快，取 ceil
        k_float = (-1 + math.sqrt(delta)) / 2
        ans = math.ceil(k_float)
        print(ans)
    except ValueError:
        break