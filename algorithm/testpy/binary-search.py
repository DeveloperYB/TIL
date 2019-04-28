def binary_search(list, target):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        chk = list[mid]
        if chk == target : # 찾는 숫자를 찾음
            return mid
        if chk > target : # 찾는 숫자가 체크한 숫자보다 작다.
            high = mid - 1
        else : # 찾는 숫자가 체크한 숫자보다 크다.
            low = mid + 1
    return None # 찾는 숫자가 배열에 없다.

test_list = [1,2,3,4,5,6,7,8,9,10,12,14,16,18,20]

print(binary_search(test_list, 5)) # 4
print(binary_search(test_list, 11)) # None
