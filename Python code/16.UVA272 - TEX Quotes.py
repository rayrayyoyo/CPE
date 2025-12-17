# -*- coding: utf-8 -*-
import sys

# 讀取整個檔案內容比較好處理跨行
text = sys.stdin.read()
result = []
first = True

for char in text:
    if char == '"':
        if first:
            result.append("``")
        else:
            result.append("''")
        first = not first
    else:
        result.append(char)

print("".join(result), end="")