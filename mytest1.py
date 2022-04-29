def squirrel(N):
    """
    the function of finding
    the first digit of the factorial
    """
    fact = 1
    for i in range(2, N + 1):
        fact = fact * i
    while fact // 10 > 0:
        fact = fact // 10
    return fact
