
"""
Program: Find Kth Largest and Min-Max
Author: Saurav 241492

Description:
Implements functions to find the kth largest element
and the minimum and maximum elements in an unsorted array.

Input: List of integers and value of k.
Output: Kth largest element and min-max pair.
"""

from typing import List, Tuple


class Find:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Return the kth largest element in nums."""
        sorted_nums = sorted(nums, reverse=True)
        return sorted_nums[k - 1]

    def findMinMax(self, nums: List[int]) -> Tuple[int, int]:
        """Return the minimum and maximum elements."""
        minimum = min(nums)
        maximum = max(nums)

        return minimum, maximum


# User Input
finder = Find()

arr = list(map(int, input("Enter the elements: ").split()))

k = int(input("Enter the value of k: "))

# Output
print(f"{k}th largest :", finder.findKthLargest(arr, k))

minimum, maximum = finder.findMinMax(arr)
print("Minimum     :", minimum)
print("Maximum     :", maximum)


