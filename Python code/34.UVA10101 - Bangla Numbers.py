# -*- coding: utf-8 -*-
import sys

def solve(n):
    if n >= 10000000:
        solve(n // 10000000)
        print(" kuti", end="")
        n %= 10000000
    if n >= 100000:
        solve(n // 100000)
        print(" lakh", end="")
        n %= 100000
    if n >= 1000:
        solve(n // 1000)
        print(" hajar", end="")
        n %= 1000
    if n >= 100:
        solve(n // 100)
        print(" shata", end="")
        n %= 100
    if n > 0:
        print(f" {n}", end="")

lines = sys.stdin.readlines()
case_num = 1
for line in lines:
    line = line.strip()
    if not line: continue
    
    val = int(line)
    # 格式要求：序號佔 4 格，靠右對齊
    print(f"{case_num:>4}.", end="")
    
    if val == 0:
        print(" 0")
    else:
        solve(val)
        print()
    case_num += 1