def solution(a, b):
    if a > b:
        big = a
        small = b
    else:
        big = b
        small = a
        
    s = 0
    for i in range(small, big+1):
        s += i
    return s