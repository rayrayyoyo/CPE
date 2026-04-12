import sys
lines = sys.stdin.readlines()
for i in range(0, len(lines), 2):
    if i + 1 >= len(lines): break 
    a = lines[i].strip()
    b = lines[i+1].strip()
    result = []
    for char_code in range(ord('a'), ord('z') + 1):
        char = chr(char_code)
        count_a = a.count(char)
        count_b = b.count(char)
        common_count = min(count_a, count_b)
        result.append(char * common_count)
    print("".join(result))