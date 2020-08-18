import numpy as np

def solution(n, costs):
    r = np.zeros((n,n))
    for i in range(len(costs)):
        r[costs[i][0]][costs[i][1]] = costs[i][2]
        print(f'r{r}')
