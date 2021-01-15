# 정렬

> 빠른 순
>
> - 버블 정렬<선택 정렬<삽입 정렬<셀 정렬<퀵 정렬<병합 정렬



### 선택 정렬 Selection Sort

주어진 배열에서 최댓값을 찾아 맨 오른쪽 값과 교체하는 과정을 반복한다. 이웃한 두 값을 정렬하지 않아서 버블정렬보다 빠르다. 반대로 최솟값을 찾아 맨 왼쪽 값과 교체할 수도 있다.

- 시간 복잡도 $n^2$

- 메모리 1

```python
def selection_sort(arr,n):
    for i in range(n-1): #0 1 2 ... n-2
        for j in range(i+1,n): #1~n-1 2~n-1 3~n-1 ... n-2~n-1
            if a[i]>a[j]:
                a[i],a[j] = a[j], a[i]
```



### 버블 정렬 Bubble Sort

이웃한 두 값을 비교하여 큰 값을 오른쪽으로 이동시키는 방법이다.

왼쪽 첫 값부터 탐색을 시작하고, 탐색을 반복한다.

- 시간 복잡도 $n\le t\le n^2$

- 메모리 1

```python
def bubble_sort(arr,n):
    for i in range(n-1): #0 1 2 ... n-2
        for j in range(n-1-i):`#0~n-2 0~n-3 0~n-4 ... 0
            if arr[j]>arr[j+1]: #이웃한 두 값 비교
                arr[j], arr[j+1] = arr[j+1], arr[j] #위치 바꾸기
```



### 삽입 정렬 Insertion Sort??

정렬된 배열에 새로운 값을 끼워넣는 방법이다. 주어진 배열이 이미 정렬된 배열에 가까울수록 빠르고, 역순일 경우 매우 느리다. 삽입정렬이 선택정렬과 버블정별보다 빠른 경향이 있다.

- 시간 복잡도 $n\le t\le n^2$

- 메모리 1

```python
def intertion_sort(arr,start,gap):
    for target in range(start+gap,len(arr),gap):
        val = arr[target] #리스트 값
        i = target #인덱스 저장
        while i>start:
            if arr[i-gap]>val: #비교 인덱스보다 크면
                arr[i] = arr[i-gap] #할당
            else:
                break
            i -= gap
        arr[i] = val #해당 값 삽입
```



### 쉘 정렬 Shell Sort

삽입 정렬의 비효율성을 개선한 방식으로, k개씩 묶은 서브 배열을 만들어서  삽입정렬을 수행한다. 정렬 후에는 간격 k를 절반으로 줄여서 다시 정렬을 반복한다.

- 시간 복잡도 $n \log n\le t\le n \log^2 n$

- 메모리 1

```python
def shell_sort(arr):
    gap = len(arr)//2 #중간값
    while gap>0:
        for start in range(gap): #중간값만큼 반복
            insertion_sort(arr,start,gap) #삽입 정렬
        gap = gap//2
```



### 병합 정렬 Merge Sort

배열의 값이 2개씩 묶일 때까지 반으로 쪼개는 작업을 반복한다.(이진탐색) 이후, 묶음의 작은 값부터 병합하는 과정을 반복한다. 분할 정복 알고리즘의 일종

- 시간 복잡도 $n \log n$

- 메모리 n

```python
def merge_sort(arr):
    if len(arr)>1:
        #반으로 쪼개기
        mid = len(arr)//2
        l_arr,r_arr = arr[:mid],arr[mid:]
        merge_sort(l_arr) #왼쪽 쪼개기>탐색
        merge_sort(r_arr) #오른쪽 쪼개기>탐색
        
        l_idx, r_idx, i = 0,0,0
        while l_idx<len(l_arr) and r_idx<len(r_arr):
            if l_arr[l_idx]<r_arr[r_idx]: #오른쪽 값이 클 경우
                arr[i] = l_arr[l_idx] #왼쪽을 앞에 붙이고
                l_idx += 1
            else: #왼쪽 값이 클 경우
                arr[i] = r_arr[r_idx]
                r_idx += 1
            i+=1 #기준 인덱스 옮기기
        arr[i:] = l_arr[l_idx:] if l_idx != len(l_arr) else r_arr[r_idx:]
```



### 퀵 정렬 Quick Sort

기준값을 설정하여 기준값보다 작으면 앞쪽에, 크면 뒤쪽에 배치한다. 이후 양쪽에 대한 작업을 반복한다. 분할 정복 알고리즘의 일종이며 재귀 1턴이 돌 때마다 해당 턴의 기준값이 최종 위치를 얻는다. 양쪽 중 한쪽에 데이터가 치우친 경우, 시간 복잡도가 증가한다.

병합정렬은 쪼갠 뒤 합치는 과정에서 정렬하지만 퀵정렬은 쪼개면서 정렬한다. 

원래 stable하지 않지만 추가 메모리를 사용하면 stable하게 사용할 수 있다.

> stable은 이미 정렬된 값과 같은 값이 들어왔을 때, 순서가 바뀌지 않는 것을 의미한다. 굴러들어온 돌이 박힌 돌을 빼낼 수 없는 상황

- 시간 복잡도 $n \log n \le t \le n \log n^2$

- 메모리 $\log n \le m \le n$


```python
def quick_sort(arr,start,end):
    if start<end:
        left = start #시작값 할당
        pivot = arr[end] #기준값 할당
        for i in range(start,end): #시작부터 끝까지
            #pivot 위치 찾기
            if arr[i]<pivot: 
                arr[i],arr[left] = arr[left],arr[i]
                left += 1 #인덱스 변경
        arr[left],arr[end] = arr[end],arr[left]
        quick_sort(arr,start,left-1) #pivot 왼쪽 탐색
        quick_sort(arr,left+1,end) #pivot 오른쪽 탐색
```
