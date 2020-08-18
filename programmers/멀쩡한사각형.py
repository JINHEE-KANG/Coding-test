import math
def solution(w,h):
    d = math.sqrt(w**2+h**2)
    x = d/w
    nh = math.sqrt(x**2-1)
    print(f'd:{d},x:{x},nh:{nh}')
    answer = 0

    for i in range(w):
        answer += int(h-nh)
        h -= nh
        print(f'add:{int(h-nh)},answer:{answer},h:{h}')
    return answer*2
