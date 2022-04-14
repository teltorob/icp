def switch(A: list) -> list:
    # ===============================================================================================================
    # Three pointer approach

    # increase left pointer and mid pointer by 1 when we find two and swap it with middle element
    # increase mid by 1 when we find 3
    # decrease right pointer by 1 and swap right and mid element
    # ===============================================================================================================
    left = 0                        # Left pointer
    mid = 0                         # mid pointer
    right = len(A) - 1              # Right pointer

    while(mid <= right):
        element = A[mid]

        if element == 2:
            A[mid], A[left] = A[left], A[mid]
            mid += 1
            left += 1

        elif element == 3:
            mid += 1

        else:
            A[mid], A[right] = A[right], A[mid]
            right -= 1

    return A
