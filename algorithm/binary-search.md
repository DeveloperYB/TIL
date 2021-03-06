# Binary search : 이진탐색 알고리즘

이진 탐색은 1~100 사이의 숫자 중 특정 숫자를 찾는다고 가정하였을 때, 1부터 탐색을 시작하는 것`(단순 탐색:simple search)`이 아닌, 중간 부터 시작하는 탐색이다.

### 예시 1)
```
준비된 배열 : [1, ... , 50, ... , 100]
(1부터 100까지의 자연수)

찾는 수 : 78
(찾는 수를 'X' 라고 지칭)

단순탐색의 경우
단순 탐색은 1부터 차례대로 78숫자가 올때까지 78번의 탐색을 시도한다.

이진탐색의 경우
1~100 사이 배열 중 가운데 50 부터 탐색을 시작
X (찾고자 하는 수) = 78 이므로,

탐색 첫번째,
X는 가운데 수 50 보다 크다 그러므로 50보다 작은 수는 제외
(탐색배열이 51 부터 100 까지로 줄었다.)
(51 ~ 100의 가운데 수 75)

탐색 두번째,
X는 가운데 수 75 보다 크다 그러므로 75보다 작은 수는 제외
(탐색배열이 76 부터 100 까지로 줄었다.)
(76 ~ 100의 가운데 수 88)

탐색 세번째,
X는 가운데 수 88 보다 작다 그러므로 88보다 큰 수는 제외
(탐색배열이 76 부터 87 까지로 줄었다.)
(76 ~ 87의 가운데 수 81)

탐색 네번째,
X는 가운데 수 81 보다 작다 그러므로 81보다 큰 수는 제외
(탐색배열이 76 부터 80 까지로 줄었다.)
(76 ~ 80의 가운데 수 78)

탐색 다섯번째,
X는 가운데 수 78과 일치한다. = 탐색 종료

이진 탐색은 5번의 탐색을 하였다.
```

한 번의 탐색으로 남은 수의 `절반씩 제외`를 시킬 수 있다.\
n개의 원소를 가진 리스트(배열)에 이진탐색을 적용하면 최대 log<sub>2</sub> n 번 으로 답을 찾을 수 있다.\
리스트의 숫자가 1024개가 있다면 log<sub>2</sub> 1024 = 10 이므로, 10번의 탐색 안에 답을 찾을 수 있다.

### 예시 2) Python3 code
```python
def binary_search(list, target):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        # // : 나눗셈 값의 숫자가 소숫점일 경우, 소숫점을 버린 정수를 반환합니다. (floor division)
        chk = list[mid]
        if chk == target : # 찾는 숫자를 찾음
            return mid
        if chk > target : # 찾는 숫자가 체크한 숫자보다 작다.
            high = mid - 1
        else : # 찾는 숫자가 체크한 숫자보다 크다.
            low = mid + 1
    return None # 찾는 숫자가 배열에 없다.

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 18, 20]

print(binary_search(test_list, 5)) # 4, 인덱스 4 = 5
print(binary_search(test_list, 11)) # None 배열 내에 11이라는 숫자는 없다.
```

극단적으로 엄청 많은 숫자를 담은 배열로 가정하자면, 400억개의 숫자를 가진 배열 중 마지막 Idx 400억 숫자를 찾을때 단순 탐색은 400억번 탐색을 하지만 이진 탐색은 35번의 탐색으로 숫자를 찾을 수 있다.

---

## 이진탐색 알고리즘 요약

- 이진탐색은 단순탐색보다 훨씬 빠르다. ( 처리속도 : log<sub>2</sub> n 이 n 보다 빠르다. )
- 이진 탐색 알고리즘은 정렬된 데이터가 아니면 적용이 불가능하다.