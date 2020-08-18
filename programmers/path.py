def find_path(st,ed,pd,m): # st: 시작점, ed: 목표지점, pd: 웅덩이 좌표, m: 이동횟수
    move = ''
    m_mv = [st[0]+1,st[1]] # 가로 이동
    n_mv = [st[0],st[1]+1] # 세로 이동
    print(f'm_mv{m_mv}, n_mv{n_mv}, move{move}')
    if (m_mv not in pd) and (n_mv not in pd):
        if ed not in [m_mv,n_mv]:
            m += 1
            print(f'm{m}')
            find_path(m_mv,ed,pd,m)
            find_path(n_mv,ed,pd,m)
        else:
            move.append(str(m))
            print(f'move{move}')
            break
    elif m_mv not in pd:
        if ed!=m_mv:
            m += 1
            print(f'm{m}')
            find_path(m_mv,ed,pd,m)
        else:
            move.append(str(m))
            print(f'move{move}')
            break
    elif n_mv not in pd:
        if ed != n_mv:
            m += 1
            print(f'm{m}')
            find_path(n_mv,ed,pd,m)
        else:
            move.append(str(m))
            print(f'move{move}')
            break
    return move
