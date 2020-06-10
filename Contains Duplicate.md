# Contains Duplicate

### 출처

LeetCode>Problems

[문제 보러가기](https://leetcode.com/problems/contains-duplicate/)



## Problem

배열 요소 중 중복되는 숫자가 존재하면 **True**, 중복되는 숫자가 존재하지 않으면 **False**를 출력하시오.

#### **Example 1:**

```
Input: [1,2,3,1]
Output: true
```

#### **Example 2:**

```
Input: [1,2,3,4]
Output: false
```

#### **Example 3:**

```
Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
```



## Code

**19.07.03 ver**

```python
int_list = list(map(int,input('input: ').split(',')))

for idx in range(len(int_list)):
    num = int_list[idx]
    if int_list.count(num)=1:
        output = False
        continue
    else:
        output = True
        break
print('Output: ',output)
```

#### 사용 함수

- `map()` 리스트 요소의 정수변환
- `split()` 문자열 자르기
- `len()` 리스트의 길이
- `count()` 리스트 속 요소 개수
