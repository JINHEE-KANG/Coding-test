def solution(operations):
    answer = []
    for i in range(len(operations)):
        t = operations[i].split(' ')
        print(f'{i}th_operation: {t}')
        if t[0]=="I":
            answer.append(int(t[1]))
            print(f'answer:{answer}')
        elif len(answer)==0:
            continue
        elif t[1]=="1":
            answer.remove(max(answer))
            print(f'answer:{answer}')
        else:
            answer.remove(min(answer))
            print(f'answer:{answer}')
    if len(answer)<2:
        mx, mn = 0, 0
    else:
        mx, mn = max(answer), min(answer)
    return [mx,mn]
