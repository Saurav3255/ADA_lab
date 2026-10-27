
"""
Program: KMP String Matching and Random Stream Sampling
Author: Saurav 241492

Description:
Implements strStr() using the Knuth-Morris-Pratt (KMP)
algorithm and Randomizer using reservoir sampling.

Input: A text and pattern, or a stream of integer elements.
Output: First pattern index or a randomly sampled stream element.
"""

from typing import Iterable, Optional
import random


def strStr(haystack: str, needle: str) -> int:
    """Return the first index of needle in haystack, or -1."""
    if needle == "":
        return 0

    # Build the longest proper prefix/suffix (LPS) array.
    lps = [0] * len(needle)
    length = 0
    i = 1

    while i < len(needle):
        if needle[i] == needle[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length > 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    # Search for the pattern in the text.
    i = j = 0

    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1

            if j == len(needle):
                return i - j

        elif j > 0:
            j = lps[j - 1]
        else:
            i += 1

    return -1


class Randomizer:
    def __init__(self, stream: Iterable[int]):
        self.stream = stream
        self._sample = None
        self._sampled = False

    def getRandom(self) -> int:
        """
        Return one uniformly sampled stream element.
        Each element must be an integer.
        """
        sample = None
        count = 0

        for count, value in enumerate(self.stream, start=1):
            if random.randrange(count) == 0:
                sample = value

        if count == 0:
            raise ValueError("Cannot sample from an empty stream.")

        self._sample = sample
        self._sampled = True
        return sample


# Main program
if __name__ == "__main__":
    haystack = input("Enter text: ")
    needle = input("Enter pattern: ")

    print("Pattern index:", strStr(haystack, needle))

    data = list(map(int, input(
        "Enter stream integers separated by spaces: "
    ).split()))

    randomizer = Randomizer(data)
    print("Random sample:", randomizer.getRandom())
