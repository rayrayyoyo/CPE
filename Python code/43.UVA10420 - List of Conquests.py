# -*- coding: utf-8 -*-
import sys

lines = sys.stdin.readlines()
if len(lines) > 0:
    n = int(lines[0])
    countries = {}
    
    for i in range(1, n + 1):
        parts = lines[i].split()
        if not parts: continue
        
        country = parts[0]
        # 只需要統計國家，後面的名字不重要
        countries[country] = countries.get(country, 0) + 1
        
    # 按字母順序輸出
    for country in sorted(countries.keys()):
        print(f"{country} {countries[country]}")