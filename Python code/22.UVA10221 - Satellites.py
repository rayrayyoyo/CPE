# -*- coding: utf-8 -*-
import sys
import math

for line in sys.stdin:
    parts = line.split()
    if len(parts) < 3:
        continue
        
    s = int(parts[0]) + 6440  # 半徑
    a = int(parts[1])         # 角度
    unit = parts[2]           # 單位

    if unit == "min":
        a /= 60.0

    # 修正重點：如果角度超過 180 度，取較小的夾角
    if a > 180:
        a = 360 - a

    # 弧長公式
    arc = 2 * math.pi * s * (a / 360.0)
    # 弦長公式 (利用三角函數)
    chord = 2 * s * math.sin(math.radians(a / 2.0))

    print(f"{arc:.6f} {chord:.6f}")