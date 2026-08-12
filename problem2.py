#Design a Sort class containing merge_sort(arr: List[int]) -> List[int] and quick_sort(arr:
List[int]) -> List[int] methods that accept an unsorted integer array and return the sorted
array.
from typing import List


class Sort:
    def merge_sort(self, arr: List[int]) -> List[int]:
        """Return a sorted copy of arr using merge sort."""
        if len(arr) <= 1:
            return arr.copy()

        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self._merge(left, right)

    def _merge(self, left: List[int], right: List[int]) -> List[int]:
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

    def quick_sort(self, arr: List[int]) -> List[int]:
        """Return a sorted copy of arr using quick sort."""
        if len(arr) <= 1:
            return arr.copy()

        pivot = arr[len(arr) // 2]

        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return (
            self.quick_sort(left)
            + middle
            + self.quick_sort(right)
        )


# Example
sorter = Sort()

arr = [5, 2, 8, 1, 3]

print(sorter.merge_sort(arr))  # [1, 2, 3, 5, 8]
print(sorter.quick_sort(arr))  # [1, 2, 3, 5, 8]
