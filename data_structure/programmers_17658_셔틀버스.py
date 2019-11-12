from collections import deque
from datetime import time

def solution(n, t, m, timetable):
    times = []
    for t in timetable:
        times.append(time(*[int(x) for x in t.split(':')]))
    print(times)
    
    
        
    