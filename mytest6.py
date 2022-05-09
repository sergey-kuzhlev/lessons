from typing import List

def PatternUnlock(N: int, hits: List[int]) -> str:
    """returns the second array sorted by the first array"""
    result = 0
    k = 1
    for i in range(N-1):
        if hits[i] == 1:
            if hits[i+1] == 5 or hits[i+1] == 8:
                result += 2 ** (0.5)
            else:
                result += 1
        if hits[i] == 2:
            if hits[i+1] == 6 or hits[i+1] == 9 or hits[i+1] == 4 or hits[i+1] == 7:
                result += 2 ** (0.5)
            else:
                result += 1
        if hits[i] == 3:
            if hits[i+1] == 5 or hits[i+1] == 8:
                result += 2 ** (0.5)
            else:
                result += 1
        if hits[i] == 4:
            if hits[i+1] == 2:
                result += 2 ** (0.5)
            else:
                result += 1
        if hits[i] == 5:
            if hits[i+1] == 1 or hits[i+1] == 3:
                result += 2 ** (0.5)
            else:
                result += 1
        if hits[i] == 6:
            if hits[i+1] == 2:
                result += 2 ** (0.5)
            else:
                result += 1
        if hits[i] == 7:
            if hits[i+1] == 2:
                result += 2 ** (0.5)
            else:
                result += 1
        if hits[i] == 8:
            if hits[i+1] == 1 or hits[i+1] == 3:
                result += 2 ** (0.5)
            else:
                result += 1
        if hits[i] == 9:
            if hits[i+1] == 2:
                result += 2 ** (0.5)
            else:
                result += 1
    result = round(result, 5)
    print(result)
    result *= 100000
    res = 0
    while result > 0:
        d = result % 10
        if d != 0:
            res += d * k
            k *= 10
        result = result // 10
    res = str(round(res))

    return res
