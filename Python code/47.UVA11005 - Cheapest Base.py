# -*- coding: utf-8 -*-
import sys

# 一次讀取所有整數
def get_all_ints():
    input_data = sys.stdin.read().split()
    if not input_data: return []
    return map(int, input_data)

def solve():
    iterator = get_all_ints()
    try:
        T_cases = next(iterator)
        for t in range(1, T_cases + 1):
            if t > 1: print() # Case 間空行
            print(f"Case {t}:")
            
            # 讀取 36 個成本
            costs = []
            for _ in range(36):
                costs.append(next(iterator))
                
            # 讀取詢問數量
            Q = next(iterator)
            for _ in range(Q):
                num = next(iterator)
                
                cheapest_cost = float('inf')
                cheapest_bases = []
                
                # 檢查 Base 2 到 36
                for base in range(2, 37):
                    current_cost = 0
                    n = num
                    
                    # 計算該進位下的成本
                    while n > 0:
                        digit = n % base
                        current_cost += costs[digit]
                        n //= base
                    
                    # 處理 num = 0 的特殊情況 (雖然題目是正整數，防禦性編程)
                    if num == 0:
                        current_cost = costs[0]
                        
                    if current_cost < cheapest_cost:
                        cheapest_cost = current_cost
                        cheapest_bases = [base]
                    elif current_cost == cheapest_cost:
                        cheapest_bases.append(base)
                        
                print(f"Cheapest base(s) for number {num}: {' '.join(map(str, cheapest_bases))}")
                
    except StopIteration:
        pass

solve()