nums = [int(_) for _ in input().split()]

nums.sort()

for ch in input():
    if ch=='A':
        print(nums[0])
    elif ch == 'B':
        print(nums[1])
    else:
        print(nums[2])