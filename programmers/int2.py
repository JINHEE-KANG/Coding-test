def solution(triangle):
    answer = 0
    dp = [triangle[0]]
    for i,rowlst in enumerate(triangle):
        if i == 0: continue
        lst = []
        rowlength = len(rowlst)-1
        print(f'rowlst{rowlst},rowlength{rowlength}')
        for k,in_value in enumerate(rowlst):
            if k==0:
                lst.append(dp[i-1][0]+in_value)
            elif k==rowlength:
                lst.append(dp[i-1][rowlength-1]+ in_value)
            else:
                lst.append(max(dp[i-1][k-1],dp[i-1][k])+in_value)
            print(f'k{k},in_value{in_value},lst{lst}')
        dp.append(lst)

    for value in dp[-1]: answer = max(answer,value)
    
    return answer
