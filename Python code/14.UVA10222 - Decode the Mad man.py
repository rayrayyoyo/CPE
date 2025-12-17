# -*- coding: utf-8 -*-
import sys

keyboard = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"

def solve():
    for line in sys.stdin:
        line = line.lower()
        for char in line:
            if char in keyboard:
                # 找到該字元在鍵盤字串的位置，然後往前推 2 格
                idx = keyboard.find(char)
                print(keyboard[idx - 2], end="")
            else:
                # 空白或換行直接輸出
                print(char, end="")
solve()