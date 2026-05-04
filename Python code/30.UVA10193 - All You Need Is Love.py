import sys
import math

# 1. 讀取所有資料並切開
data = sys.stdin.read().split()

n_cases = int(data[0]) # 第一個數字是測試組數
idx = 1 # 指向第一組字串的書籤

for i in range(1, n_cases + 1):
    s1 = data[idx]
    s2 = data[idx+1]
    idx += 2 # 讀完兩組字串，書籤往後移兩格
    
    # 2. 將二進位字串轉為十進位整數
    n1 = int(s1, 2)
    n2 = int(s2, 2)
    
    # 3. 判斷最大公因數是否大於 1
    if math.gcd(n1, n2) > 1:
        print(f"Pair #{i}: All you need is love!")
    else:
        print(f"Pair #{i}: Love is not all you need!")