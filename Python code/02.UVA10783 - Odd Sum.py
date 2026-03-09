case = int(input())
for i in range(case):
    A, B = int(input()), int(input())
    sum = 0
    for k in range(A, B + 1, 1):
        if k % 2 == 1:
            sum += k
    print(f"Case {i + 1}:", sum)