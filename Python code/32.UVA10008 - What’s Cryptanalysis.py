# -*- coding: utf-8 -*-
import sys
from collections import Counter

# 讀取全部輸入
lines = sys.stdin.readlines()
text = "".join(lines)

# 略過第一行的數字 (行數)，直接統計所有文字
# 找到第一個換行符的位置，切掉第一行
first_newline = text.find('\n')
if first_newline != -1:
    content = text[first_newline+1:]
else:
    content = ""

# 統計字母 (只看 A-Z)
counts = Counter()
for char in content:
    if char.isalpha():
        counts[char.upper()] += 1

# 排序：次數(大->小)，字母(A->Z)
# Python sort 是穩定的，可以先對字母排，再對次數排
items = list(counts.items())
# 1. 先按字母升序
items.sort(key=lambda x: x[0])
# 2. 再按次數降序
items.sort(key=lambda x: x[1], reverse=True)

for char, count in items:
    print(f"{char} {count}")