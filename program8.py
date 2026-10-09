
"""
Program: Huffman Coding
Author: Saurav 241492

Description:
Implements Huffman Coding using a binary tree and a min-heap.
Generates prefix-free binary codes based on character frequencies.

Input: Dictionary of characters and their frequencies.
Output: Binary encoding dictionary for each character.
"""

from typing import Dict
import heapq


# Node class for Huffman Tree
class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right


class HuffmanCoder:
    def __init__(self):
        self.root = None
        self.codes = {}

    # Build Huffman Tree
    def build_tree(self, frequencies: Dict[str, int]) -> Node:
        if not frequencies:
            raise ValueError("Frequency dictionary cannot be empty.")

        if any(freq <= 0 for freq in frequencies.values()):
            raise ValueError("Frequencies must be positive.")

        heap = []
        counter = 0

        for char, freq in frequencies.items():
            heapq.heappush(heap, (freq, counter, Node(char, freq)))
            counter += 1

        while len(heap) > 1:
            freq1, _, left = heapq.heappop(heap)
            freq2, _, right = heapq.heappop(heap)

            merged = Node(None, freq1 + freq2, left, right)

            heapq.heappush(
                heap, (merged.freq, counter, merged)
            )
            counter += 1

        self.root = heap[0][2]
        self.codes = {}
        return self.root

    # Generate Huffman Codes
    def generate_codes(self) -> Dict[str, str]:
        if self.root is None:
            raise ValueError("Build the Huffman tree first.")

        codes = {}

        def traverse(node, code):
            if node.char is not None:
                codes[node.char] = code if code else "0"
                return

            traverse(node.left, code + "0")
            traverse(node.right, code + "1")

        traverse(self.root, "")
        self.codes = codes
        return codes


# Main program
if __name__ == "__main__":
    frequencies = {
        'A': 5,
        'B': 9,
        'C': 12,
        'D': 13,
        'E': 16,
        'F': 45
    }

    coder = HuffmanCoder()

    coder.build_tree(frequencies)
    codes = coder.generate_codes()

    print("Character Frequencies:", frequencies)
    print("\nHuffman Codes:")

    for char, code in sorted(codes.items()):
        print(f"{char}: {code}")