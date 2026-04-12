import sys
keyboard = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
def solve():
    for line in sys.stdin:
        line = line.lower()
        for char in line:
            if char in keyboard:
                idx = keyboard.find(char)
                print(keyboard[idx - 2], end="")
            else:
                print(char, end="")
solve()