
"""
Program: Strassen Matrix Multiplication
Author: Saurav 241492

Description:
Implements Strassen's Matrix Multiplication algorithm.

Input: Two square matrices of size 2^n.
Output: Product matrix using Strassen's algorithm.
"""

from typing import List


class Matrix:
    def strassen_multiply(
        self,
        A: List[List[int]],
        B: List[List[int]]
    ) -> List[List[int]]:

        n = len(A)

        if n == 1:
            return [[A[0][0] * B[0][0]]]

        mid = n // 2

        A11 = [row[:mid] for row in A[:mid]]
        A12 = [row[mid:] for row in A[:mid]]
        A21 = [row[:mid] for row in A[mid:]]
        A22 = [row[mid:] for row in A[mid:]]

        B11 = [row[:mid] for row in B[:mid]]
        B12 = [row[mid:] for row in B[:mid]]
        B21 = [row[:mid] for row in B[mid:]]
        B22 = [row[mid:] for row in B[mid:]]

        # Strassen's seven multiplications
        M1 = self.strassen_multiply(
            self.add(A11, A22),
            self.add(B11, B22)
        )

        M2 = self.strassen_multiply(
            self.add(A21, A22),
            B11
        )

        M3 = self.strassen_multiply(
            A11,
            self.subtract(B12, B22)
        )

        M4 = self.strassen_multiply(
            A22,
            self.subtract(B21, B11)
        )

        M5 = self.strassen_multiply(
            self.add(A11, A12),
            B22
        )

        M6 = self.strassen_multiply(
            self.subtract(A21, A11),
            self.add(B11, B12)
        )

        M7 = self.strassen_multiply(
            self.subtract(A12, A22),
            self.add(B21, B22)
        )

        # Calculate result sub-matrices
        C11 = self.add(self.subtract(self.add(M1, M4), M5), M7)
        C12 = self.add(M3, M5)
        C21 = self.add(M2, M4)
        C22 = self.add(
            self.subtract(self.add(M1, M3), M2),
            M6
        )

        # Combine sub-matrices
        result = []

        for i in range(mid):
            result.append(C11[i] + C12[i])

        for i in range(mid):
            result.append(C21[i] + C22[i])

        return result

    def add(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        """Add two matrices."""
        return [
            [A[i][j] + B[i][j] for j in range(len(A))]
            for i in range(len(A))
        ]

    def subtract(
        self,
        A: List[List[int]],
        B: List[List[int]]
    ) -> List[List[int]]:
        """Subtract two matrices."""
        return [
            [A[i][j] - B[i][j] for j in range(len(A))]
            for i in range(len(A))
        ]
    
matrix = Matrix()
n = int(input("Enter the size of matrix (power of 2): "))

print("Enter Matrix A:")
A = []

for i in range(n):
    row = list(map(int, input(f"Row {i + 1}: ").split()))
    A.append(row)

print("Enter Matrix B:")
B = []

for i in range(n):
    row = list(map(int, input(f"Row {i + 1}: ").split()))
    B.append(row)


# Calculate product
C = matrix.strassen_multiply(A, B)

print("\nProduct Matrix:")
for row in C:
    print(*row)
