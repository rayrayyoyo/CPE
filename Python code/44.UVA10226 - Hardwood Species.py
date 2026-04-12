import sys

# 一次讀進來，用 splitlines 拆成一行一行的清單
input_data = sys.stdin.read().splitlines()

# 第一行是 Case 數量 T
T = int(input_data[0])

# 從第 3 行開始才是真正的資料（跳過 T 後面的空行）
current_row = 2
for t in range(T):
    if t > 0: print() # 題目要求：Case 之間要印一個空行
    
    trees = {} # 用字典來記數：{樹名: 次數}
    total = 0  # 總棵數
    
    # 讀取這一組的樹，直到遇到空行或資料結束
    while current_row < len(input_data) and input_data[current_row] != "":
        name = input_data[current_row]
        trees[name] = trees.get(name, 0) + 1 # 有就加1，沒有就設為0再加1
        total += 1
        current_row += 1
    
    # 題目要求按字母排序
    for name in sorted(trees.keys()):
        # 計算百分比，保留小數點後四位
        percent = (trees[name] / total) * 100
        print(f"{name} {percent:.4f}")
    
    current_row += 1 # 跳過組與組之間的空行