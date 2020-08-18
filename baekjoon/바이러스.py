n,e = int(input()),int(input())
links = {}
for i in range(e):
    link = list(map(int,input().split(' ')))
    print(link)
    if link[0] and link[1] not in links.keys(): #둘 다 신규
        links[link[0]] = link[1]
        links[link[1]] = link[0]
    elif link[0] not in links.keys(): # 1번째 신규
        links[link[0]] = link[1]
        links[link[1]].append(link[0])
    elif link[1] not in links.keys(): # 2번째 신규
        links[link[1]] = link[0]
        links[link[0]].append(link[1])
    else:                             # 둘 다 있음
        links[link[0]].append(link[1])
        links[link[1]].append(link[0])

#입력을 받아서 1과 연결되어 있으면 1과 연결된 값으로 바꾸고

def computer(start):
    visited = [start] #시작점부터 시작
    queue= [start]

    while queue:
        
        queue.append(links[
    

    return end

computer(1)
