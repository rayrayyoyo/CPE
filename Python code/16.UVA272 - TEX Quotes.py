import sys

text = sys.stdin.read()
result = []
first = True

for char in text:
    if char == '"':
        if first:
            result.append("``")
        else:
            result.append("''")
        first = not first
    else:
        result.append(char)

print("".join(result), end="")