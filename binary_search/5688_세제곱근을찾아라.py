for t in range(1, int(input())+1):
    n = int(input())

    left = 1
    right = int(n**(1/2))
    while left <= right:
        mid = (left+right)//2
        if mid**3 < n:
            left = mid+1
        elif mid**3 > n:
            right = mid-1
        else:
            print('#{} {}'.format(t, mid))
            break
    else:
        print('#{} {}'.format(t, -1))
    