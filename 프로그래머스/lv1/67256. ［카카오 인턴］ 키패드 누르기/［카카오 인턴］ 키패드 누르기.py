def solution(numbers, hand):
    hand = 'L' if hand=='left' else 'R'
    #  1   2   3    4   5   6    7   8   9    *   0   #
    # 0,1 0,2 1,0  1,1 1,2 2,0  2,1 2,2 3,0      0,0
    # 0,0 0,1 0,2  1,0 1,1 1,2  2,0 2,1 2,2  3,0 3,1 3,2
    answer = ''
    i = 0
    
    left = [3,0]
    right = [3,2]
    
    for n in numbers:
        if n % 3 == 1: #1,4,7
            answer += 'L'
            left = [n//3, 0]
            
        elif n>0 and n % 3 == 0: #3,6,9
            answer += 'R'
            right = [n//3-1, 2]
            
        else: #2,5,8,0
            lx, ly = left
            rx, ry = right
            tx = n//3 if n>0 else 3
            ty = n%3-1 if n>0 else 1
            
            if (abs(lx-tx)+abs(ly-ty)) > (abs(rx-tx)+abs(ry-ty)):
                answer += 'R'
                right = [tx,ty]
            elif (abs(lx-tx)+abs(ly-ty)) < (abs(rx-tx)+abs(ry-ty)):
                answer += 'L'
                left = [tx,ty]
            else:
                answer += hand
                if hand=='R': right = [tx,ty]
                else: left = [tx,ty]
    
    
    return answer