
def isqrt(i) -> int:                                # Function recursively calculates i for m = n/4
    if i < 2:
        return i
    if i * i <= m and m < (i + 1) * (i + 1):
        return i
    return isqrt(i - 1)


def main(n) -> int:
    global m

    m = n // 4
    i = isqrt(m)

    low = 2 * i                                    # 2i
    high = (2 * i) + 1                             # 2i + 1

    int_sqrt = low if low ** 2 <= n and n < high ** 2 else high
    return int_sqrt


if __name__ == "__main__":                          # Driver code
    n = int(input('Please enter your number: '))
    print(main(n))
