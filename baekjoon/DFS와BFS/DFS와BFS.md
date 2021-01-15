# [DFS와 BFS](https://www.acmicpc.net/problem/1260)

| 시간 제한 | 메모리 제한 | 제출  | 정답  | 맞은 사람 | 정답 비율 |
| --------- | ----------- | ----- | ----- | --------- | --------- |
| 2 초      | 128 MB      | 86574 | 28391 | 16516     | 31.453%   |

### 문제

그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

#### 입력

첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

#### 출력

첫째 줄에 DFS를 수행한 결과를, 그다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.



#### 예제1

```
4 5 1
1 2
1 3
1 4
2 4
3 4
```

```
1 2 4 3
1 2 3 4
```



#### 예제2

```
5 5 3
5 4
5 2
1 2
3 4
3 1
```

```
3 1 2 5 4
3 1 4 2 5
```



#### 예제3

```
1000 1 1000
999 1000
```

```
1000 999
1000 999
```

 

## CODE

```python
# bfs - 큐 이용
def bfs(start):										
    visited = [start]
    queue = [start]
    while queue:
        n = queue.pop(0)-1
        for c in range(len(matrix[start-1])):
            if matrix[n][c] == 1 and (c+1 not in visited):
                visited.append(c+1)
                queue.append(c+1)					
    return visited

# dfs - 재귀함수 이용
def dfs(start, visited):							
    visited += [start]
    for c in range(len(matrix[start-1])):
        if matrix[start-1][c] == 1 and (c+1 not in visited):
            dfs(c, visited)							
    return visited


# input
from sys import stdin
n, m, v = map(int, stdin.readline().split())		# n,m,v 할당
matrix = [[0] * (n + 1) for _ in range(n + 1)]		# 인덱스 일치를 위해 n+1사용(n+1*n+1)
for _ in range(m): # 노드 입력
    line = list(map(int, stdin.readline().split()))	# 입력값
    matrix[line[0]][line[1]] = 1					
    matrix[line[1]][line[0]] = 1 # inverse->노드 행렬 완료

# output
print(dfs(v,[]))
print(bfs(v))
```
