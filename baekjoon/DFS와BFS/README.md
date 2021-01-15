# DFS 깊이 우선 탐색

DFS는 재귀방식으로 깊게 파고들어가는 형식의 탐색 방법이다. 

시작점부터 탐색하면서 탐색 대상이 되는 값을 찾으면 <u>그 값과 연결된 다음 값을 찾을 때까지</u> 탐색을 반복한다. 점 간의 연결 구조를 탐색하는데 용이하다고 할 수 있다.

주로 **영역 나누기** 문제에 많이 쓰인다.

```python
def dfs(start, answer):							
    answer += [start] # 탐색 순서 초기값 설정
    for c in range(len(matrix[start-1])): # 정점 c 지정
        if matrix[start-1][c] == 1 and (c+1 not in answer):
            dfs(c, answer)							
    return answer # dfs 탐색 순서 반환
```

#### 문제
- [DFS와 BFS](baekjoon/DFS와BFS/DFS와BFS.md)


# BFS 너비 우선 탐색

BFS는 큐에 현재 위치를 입력하는 방식으로 탐색을 진행하는 알고리즘이다. 

DFS와 다른 점은, DFS는 탐색 가능한 점을 발견하면 그 점과 연결된 점을 새로운 탐색 대상으로 바꾸면서 반복되는 반면, BFS는 탐색 대상인 점에 대해 탐색을 모두 마친 후에 다음 좌표로 이동한다는 것이다. 

즉, 해당 점에 연결된 점을 모두 찾을 때까지 반복한다는 점이 DFS와 다르다.

BFS는 주로 **최단거리** 문제에 쓰인다.

```python
def bfs(start):										
    visited = [start] # 처음 시작-방문 list
    queue = [start] # queue-현재 위치(시작점)
    while queue: # queue가 빌 때까지-더이상 추가할 정점이 없으면 끝
        n = queue.pop(0)-1 # 정점 n 지정
        for c in range(len(matrix[start-1])): # 정점 n과 연결된 점 모두 찾기
            if matrix[n][c] == 1 and (c+1 not in visited):
                visited.append(c+1) # 순서 포함
                queue.append(c+1)					
    return visited # bfs 탐색 순서 반환
```

#### 문제
- [DFS와 BFS](baekjoon/DFS와BFS/DFS와BFS.md)
