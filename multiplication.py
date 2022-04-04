# Multiplication with addition
def multiply(a, b):
    if b == 0 or a == 0:
        return 0
    if b == 1:
        return a
    if a == 1:
        return b
    if b % 2 == 0:
        return multiply(a, b // 2) + multiply(a, b // 2)
    else:
        return a + multiply(a, b - 1)


if __name__ == "__main__":
    multiply(5, 7)
