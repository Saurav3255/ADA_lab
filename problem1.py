
"""
Program: Binary Search and Fast Power
Author: Saurav 241492

Description:
Implements Binary Search and Fast Power algorithms using iteration.

Input: Sorted list, target value, base, and exponent.
Output: Target index/status and calculated power.
"""

from typing import List

# Function to search for target using Binary Search
def search(nums: List[int], target: int) -> int:
   
    left = 0
    right = len(nums) - 1

    
    while left <= right:
        # Find the middle index
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        # If target is greater, search in the right half
        elif nums[mid] < target:
            left = mid + 1

        # Otherwise, search in the left half
        else:
            right = mid - 1

    return -1


# Function to calculate x raised to the power n
def myPow(x: float, n: int) -> float:
    # Handle negative exponent
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


# Testing Binary Search
print(search([-1, 0, 3, 5, 9, 12], 9))

# Testing Fast Power
print(myPow(2.0, 10))
