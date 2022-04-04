def divide(x, y):
    if x == 0:
        return 0, 0
    else:
        q, r = divide(x // 2, y)
        q1, r1 = 2*q, 2*r

        if x % 2 == 1:
            r2 = r1 + 1

            if r2 < y:
                return q1, r2
            else:
                return q1 + 1, r2 - y

        elif r1 < y:
            return q1, r1
        else:
            return q1 + 1, r1 - y


if __name__ == "__main__":
    print(divide(10, 3))
