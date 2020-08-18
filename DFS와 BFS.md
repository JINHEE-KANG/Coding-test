# DFS와 BFS

| 시간 제한 | 메모리 제한 | 제출  | 정답  | 맞은 사람 | 정답 비율 |
| --------- | ----------- | ----- | ----- | --------- | --------- |
| 2 초      | 128 MB      | 86574 | 28391 | 16516     | 31.453%   |

## 문제

그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

### 입력

첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

### 출력

첫째 줄에 DFS를 수행한 결과를, 그다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.



#### 예제1

##### 입력

```
4 5 1
1 2
1 3
1 4
2 4
3 4
```

##### 출력

```
1 2 4 3
1 2 3 4
```



#### 예제2

##### 입력

```
5 5 3
5 4
5 2
1 2
3 4
3 1
```

##### 출력

```
3 1 2 5 4
3 1 4 2 5
```



#### 예제3

##### 입력

```
1000 1 1000
999 1000
```

##### 출력

```
1000 999
1000 999
```

 

### CODE

[출처: 차밍이](https://chancoding.tistory.com/59)

```python
from sys import stdin								# input받기 위한 모듈
n, m, v = map(int, stdin.readline().split())		# n,m,v 할당
matrix = [[0] * (n + 1) for _ in range(n + 1)]		# 인덱스 일치를 위해 n+1사용(n+1*n+1)
for _ in range(m):									# 노드 입력
    line = list(map(int, stdin.readline().split()))	# 입력값
    matrix[line[0]][line[1]] = 1					
    matrix[line[1]][line[0]] = 1					# inverse->노드 행렬 완료

def bfs(start):										# bfs: 시작점 받기
    visited = [start]								# 순서 초기값 설정
    queue = [start]									# queue 초기값 설정
    while queue:									# queue가 빌 때까지
        n = queue.pop(0)							# queue의 1번째 값 - 정점 n 지정
        for c in range(len(matrix[start])):			# 정점 c 지정
            if matrix[n][c] == 1 and (c not in visited):	# 정점 n과 c에 노드 존재/순서x
                visited.append(c)					# 순서 포함
                queue.append(c)						# queue 퐘
    return visited									# bfs 탐색 순서 반환

def dfs(start, visited):							# dfs: 시작점, 탐색 순서
    visited += [start]								# 탐색 순서 초기값 설정
    for c in range(len(matrix[start])):				# 정점 c 지정
        if matrix[start][c] == 1 and (c not in visited):	#시작점과 c의 노드 존재/순서x
            dfs(c, visited)							# 재귀함수: 시작점을 정점 c로(반복)
    return visited									# dfs 탐색 순서 반환

print(*dfs(v,[]))
print(*bfs(v))
```