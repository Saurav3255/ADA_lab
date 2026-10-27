
"""
Program: Longest Increasing Subsequence (LIS)
Author: Saurav 241492

Description:
Finds the length of the longest strictly increasing
subsequence using binary search and dynamic programming.

Input: A list of integers.
Output: Length of the longest increasing subsequence.
"""

from typing import List
from bisect import bisect_left


def lengthOfLIS(nums: List[int]) -> int:
    tails = []

    for num in nums:
        index = bisect_left(tails, num)

        if index == len(tails):
            tails.append(num)
        else:
            tails[index] = num

    return len(tails)


# Main program
if __name__ == "__main__":
    nums = list(map(int, input("Enter integers separated by spaces: ").split()))

    result = lengthOfLIS(nums)
    print("Length of LIS:", result)
