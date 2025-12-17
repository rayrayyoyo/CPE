# -*- coding: utf-8 -*-
import sys

input_data = sys.stdin.read().split()
iterator = iter(input_data)

try:
    T = int(next(iterator))
    for _ in range(T):
        N = int(next(iterator)) # 總天數
        P = int(next(iterator)) # 政黨數
        
        hartals = set()
        
        for _ in range(P):
            h = int(next(iterator))
            # 把該政黨的所有罷工日加入集合
            for day in range(h, N + 1, h):
                # 扣除星期五(6) 和 星期六(0 mod 7)
                # 題目定義 Day 1 = Sunday
                # 1=Sun, 2=Mon ... 6=Fri, 7=Sat
                if day % 7 != 6 and day % 7 != 0:
                    hartals.add(day)
                    
        print(len(hartals))
except StopIteration:
    pass