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



## Summary

- Loop Invariant
- Linear Search
- Sorting
- Hash Table



## [Solution](https://leetcode.com/problems/contains-duplicate/solution/)

#### Approach #1 

**(Naive Linear Search) [Time Limit Exceeded 문제 발생]**

**Intuition**

*n* 개의 정수 배열의 경우의 수는  
$$
C(n,2) = \frac{n(n+1)}{2}
$$
 개이다. 따라서 총
$$
\frac{n(n+1)}{2}
$$
 개의 배열에서 중복된 쌍이 있는지 확인할 수 있다.

##### **Algorithm**

**linear search algorithm**: 원하는 요소가 발견될 때까지 각각의 요소를 한 번에 하나씩 순서대로 점검하여 특정 값이 목록에 있는지 알아내는 방법

예를 들어 *i* 번째 정수의 경우, 이전 *i-1*개의 정수에서 `nums[i]`의 중복을 검색한다. 중복이 탐색되지 않을 경우 프로그램이 계속되며 종료 시 `False`를 반환한다.

To prove the correctness of the algorithm, we define the loop invariant. A loop invariant is a property that holds before (and after) each iteration. Knowing its invariant(s) is essential for understanding the effect of a loop. Here is the *loop invariant*:

> Before the next search, there are no duplicate integers in the searched integers.

The loop invariant holds true before the loop because there is no searched integer. Each time through the loop we look for any any possible duplicate of the current element. If we found a duplicate, the function exits by returning true; If not, the invariant still holds true.

Therefore, if the loop finishes, the invariant tells us that there is no duplicate in all n*n* integers.

##### **Complexity Analysis**

- Time complexity : 
  $$
  O(n^2)
  $$
  In the worst case, there are 
  $$
  \frac{n(n+1)}{2}
  $$
  pairs of integers to check.

- Space complexity : 
  $$
  O(1)
  $$
  We only used constant extra space.

##### **Note**

This approach will get Time Limit Exceeded on LeetCode. Usually, if an algorithm is 
$$
O(n^2)
$$
, it can handle *n* up to around 
$$
10^4
$$
It gets Time Limit Exceeded when 
$$
n \geq 10^5
$$


#### Approach #2 

**(Sorting) [Accepted]**

**Intuition**

If there are any duplicate integers, they will be consecutive after sorting.

##### **Algorithm**

This approach employs sorting algorithm. Since comparison sorting algorithm like *heapsort* is known to provide 
$$
O(n \log n)
$$
 worst-case performance, sorting is often a good preprocessing step. After sorting, we can sweep the sorted array to find if there are any two consecutive duplicate elements.

##### **Complexity Analysis**

- Time complexity : 
  $$
  O(n \log n)
  $$
  Sorting is 
  $$
  O(n \log n)
  $$
  and the sweeping is 
  $$
  O(n)
  $$
  The entire algorithm is dominated by the sorting step, which is 
  $$
  O(n \log n)
  $$

- Space complexity : 
  $$
  O(1)
  $$
  Space depends on the sorting implementation which, usually, costs 
  $$
  O(1)
  $$
  auxiliary space if `heapsort` is used.

##### **Note**

The implementation here modifies the original array by sorting it. In general, it is not a good practice to modify the input unless it is clear to the caller that the input will be modified. One may make a copy of `nums` and operate on the copy instead.



#### Approach #3 

**(Hash Table) [Accepted]**

**Intuition**

Utilize a dynamic data structure that supports fast search and insert operations.

##### **Algorithm**

From [Approach #1](https://leetcode.com/problems/contains-duplicate/solution/#approach-1-naive-linear-search-time-limit-exceeded) we know that search operations is 
$$
O(n)
$$
in an unsorted array and we did so repeatedly. Utilizing a data structure with faster search time will speed up the entire algorithm.

There are many data structures commonly used as dynamic sets such as Binary Search Tree and Hash Table. The operations we need to support here are `search()` and `insert()`. For a self-balancing Binary Search Tree, `search()` and `insert()` are both 
$$
O(\log n)
$$
 time. For a Hash Table, `search()` and `insert()` are both 
$$
O(1)
$$
on average. Therefore, by using hash table, we can achieve linear time complexity for finding the duplicate in an unsorted array.

##### **Complexity Analysis**

- Time complexity : 
  $$
  O(n)
  $$
  We do `search()` and `insert()` for *n* times and each operation takes constant time.

- Space complexity : 
  $$
  O(n)
  $$
  The space used by a hash table is linear with the number of elements in it.

##### **Note**

For certain test cases with not very large *n*, the runtime of this method can be slower than [Approach #2](https://leetcode.com/problems/contains-duplicate/solution/#approach-2-sorting-accepted). The reason is hash table has some overhead in maintaining its property. One should keep in mind that real world performance can be different from what the Big-O notation says. The Big-O notation only tells us that for *sufficiently* large input, one will be faster than the other. Therefore, when *n* is not sufficiently large, an 
$$
O(n)
$$
 algorithm can be slower than an 
$$
O(n \log n)
$$
 algorithm.