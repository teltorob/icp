def isperfect(num: int)-> bool:
    sum_of_factors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_factors += i
        
    if sum_of_factors == num: return True
    return False
if __name__ == '__main__':
    inp = int(input('Please enter a number'))
    res = isperfect(inp)
    print(res)

