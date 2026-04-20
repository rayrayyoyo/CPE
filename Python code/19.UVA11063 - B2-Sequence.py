import sys
case_num = 1
input_data = sys.stdin.read().split()
iterator = iter(input_data)
try:
    while True:
        N = int(next(iterator))
        nums = []
        for _ in range(N):
            nums.append(int(next(iterator)))
        is_b2 = True
        if nums[0] < 1:
            is_b2 = False
        for k in range(N - 1):
            if nums[k] >= nums[k+1]:
                is_b2 = False
                break       
        if is_b2:
            sums = set()
            for i in range(N):
                for j in range(i, N):
                    s = nums[i] + nums[j]
                    if s in sums:
                        is_b2 = False
                        break
                    sums.add(s)
                if not is_b2:
                    break
        if is_b2:
            print(f"Case #{case_num}: It is a B2-Sequence.")
        else:
            print(f"Case #{case_num}: It is not a B2-Sequence.")
        print() 
        case_num += 1        
except StopIteration:
    pass