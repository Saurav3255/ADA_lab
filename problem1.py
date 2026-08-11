#1. Implement search(nums: List[int], target: int) -> int and myPow(x: float, n: int) ->
float functions taking an integer array/target and base/exponent pairs, returning index and computed
value respectively.
from typing import List

def search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def myPow(x: float, n: int) -> float:
    if n < 0:
        x = 1 / x
        n = -n

    result = 1.0

    while n > 0:
        if n % 2 == 1:
            result *= x

        x *= x
        n //= 2

    return result


# Testing
print(search([-1, 0, 3, 5, 9, 12], 9))
print(myPow(2.0, 10))
