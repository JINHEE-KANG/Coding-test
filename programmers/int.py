def solution(triangle):
    floor = len(triangle)
    answer = 0
    i = 0
    for n in range(floor-1):
        answer += triangle[n][i]
        t = max([triangle[n+1][i],triangle[n+1][i+1]])
        i = triangle[n+1].index(t)
        print(f'n{n}|answer{answer},t{t},i{i}')
    return answer
