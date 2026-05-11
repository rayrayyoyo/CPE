import sys

data = map(int, sys.stdin.read().split())

cases_count = next(data, None)

if cases_count is not None:
    for _ in range(cases_count):
        L = next(data)
        arr = [next(data) for _ in range(L)]
        swaps = 0
        for i in range(L):
            for j in range(L - 1 - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swaps += 1
        print(f"Optimal train swapping takes {swaps} swaps.")