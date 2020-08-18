def solution(N, stages):
    stages.sort()   #오름차순 정렬
    fail = {}       #스테이지별 실패율을 담을 dict.
    st = 1          #기본 스테이지 1
    
    while True:
        for i in range(len(stages)):        #stages길이를 반복 체크
            if stages[i]>st:                #현재 스테이지를 통과한 인덱스
                if i==0:                    #통과하지 못한 유저가 없을 때
                    fail[st] = 0            #해당 스테이지 실패율=0
                else:                       #통과하지 못한 유저가 있을 때
                    fail[st] = i/len(stages)#실패율
                    stages = stages[i:]     #통과하지 못한 유저 자르기
                break                       
            elif i+1 == len(stages):        #남은 유저 모두 통과하지 못했을 때
                fail[st] = 1                #실패율
                break
            elif len(stages)==0:            #도달한 유저가 없을 경우
                fail[st] = 0
                break
        st += 1                             #다음 스테이지 이동
        if st>N: break                      #다음 스테이지>N일 경우
            
    answer = sorted(fail.items(), key=lambda item: item[1], reverse=True)
    answer = [i[0] for i in answer]
        
    return answer
