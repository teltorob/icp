def multiply(l1: list, l2: list, result: list, place: int):

    if (len(l2) == 0):
        return result
    cur = l2.pop()

    def helper(li, mtpr, res, p):
        while (p != 0):
            res.append(0)
            p -= 1

        carry = 0
        temp = li[:]
        while (len(temp) != 0):
            c = temp.pop()
            r = c * mtpr + carry

            carry = r // 10
            res.append(r % 10)

        if carry != 0:
            res.append(carry)
        return res

    result.append(helper(l1, cur, [], place))
    place += 1
    return multiply(l1, l2, result, place)


print(multiply([3, 2, 3], [2, 5, 8], [], 0))
