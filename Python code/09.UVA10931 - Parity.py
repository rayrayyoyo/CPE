# -*- coding: utf-8 -*-
while 1:
    try:
        # 讀取輸入並轉為整數
        name = int(input())
    except EOFError:
        break

    # 題目要求：當讀到 0 時結束程式
    if name == 0:
        break
    
    # bin(name) 會把整數轉成二進位字串
    # 例如：bin(21) 會變成字串 "0b10101"
    name = bin(name)
    
    # name[2:] 是字串切片，用來去掉開頭的 "0b"
    # name.count("1") 用來計算字串裡面有幾個 "1"
    print("The parity of", name[2:], "is", name.count("1"), "(mod 2).")