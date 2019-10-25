n , m = [int(_) for _ in input().split()]
packs, pieces = [], []
for _ in range(m):
    pa, pi =[int(__) for __ in input().split()]
    packs.append(pa)
    pieces.append(pi)
mpa, mpi = min(packs), min(pieces)
# 패키지가 낱개보다 싼 경우
if mpa <= mpi:
    if n % 6 == 0:
        print(mpa*(n//6))
    else:
        print(mpa*(n//6+1))
# 패키지보다 낱개 6개가 싼 경우
elif mpa >= 6*mpi:
    print(n*mpi)
# 패키지가 낱개 6개보다 싸고 낱개가 패기지보다 싼 경우
else: #  mpi < mpa < 6*mpi
    if mpa*(n//6+1) < mpa*(n//6) + mpi*(n%6):
        print(mpa*(n//6+1))
    else:
        print(mpa*(n//6) + mpi*(n%6))