# -*- coding: utf-8 -*-
import sys

# 讀取所有行，保留原始格式（含空白）
lines = sys.stdin.readlines()
# 去掉最後的換行符，但保留每行中間或尾端的空白
lines = [line.strip('\n').strip('\r') for line in lines]

if not lines:
    sys.exit(0)

max_len = max(len(line) for line in lines)

# 旋轉邏輯：
# 新的第一行由原句的最後一句的第一個字、倒數第二句的第一個字...組成
# 其實就是轉置矩陣 (Transposition) 加上反轉順序
for col in range(max_len):
    output_line = ""
    # 從最後一行往回讀到第一行
    for row in range(len(lines) - 1, -1, -1):
        line = lines[row]
        if col < len(line):
            output_line += line[col]
        else:
            output_line += " " # 不夠長補空白
    print(output_line)