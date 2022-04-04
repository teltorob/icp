def check_perfect(num):
    sum = 0
    i = 1
    while i < num:
        if num % i == 0:
            sum += i
        i += 1
    if sum == num:
        return True
    else:
        return False
