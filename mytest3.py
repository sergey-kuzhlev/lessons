from typing import List

def ConquestCampaign(N: int, M: int, L: int, battalion: List[int]) -> int:
    """Get beachhead size and occupied cells
    and return the day then all cells are occupied.
    In one day occupied cells that are adjoin horizontally and vertically"""

    delet = []
    day = 1
    am = 0
    for i in range(0, len(battalion), 2):
        for j in range(i + 2, len(battalion), 2):
            if battalion[i] == battalion[j] and battalion[i + 1] == battalion[j + 1]:
                delet.append(j)
    for d in delet:
        battalion[d] = 0
        battalion[d + 1] = 0
    while 0 in battalion:
        battalion.remove(0)
    if (len(battalion)//2) == (M * N):
        return 1

    while M * N * 2 != len(battalion):
        for i in range(am, len(battalion), 2):
            if battalion[i] == 1 and battalion[i+1] == 1:
                battalion.append(1)
                battalion.append(2)
                battalion.append(2)
                battalion.append(1)
            elif battalion[i] == 1 and battalion[i+1] == M:
                battalion.append(1)
                battalion.append(battalion[i+1] - 1)
                battalion.append(2)
                battalion.append(battalion[i+1])
            elif battalion[i] == N and battalion[i+1] == 1:
                battalion.append(battalion[i] - 1)
                battalion.append(1)
                battalion.append(battalion[i])
                battalion.append(2)
            elif battalion[i] == N and battalion[i+1] == M:
                battalion.append(battalion[i])
                battalion.append(battalion[i+1] - 1)
                battalion.append(battalion[i] - 1)
                battalion.append(battalion[i+1])
            elif battalion[i] == 1:
                battalion.append(2)
                battalion.append(battalion[i+1])
                battalion.append(1)
                battalion.append(battalion[i+1] - 1)
                battalion.append(1)
                battalion.append(battalion[i+1] + 1)
            elif battalion[i+1] == 1:
                battalion.append(battalion[i])
                battalion.append(2)
                battalion.append(battalion[i] + 1)
                battalion.append(1)
                battalion.append(battalion[i] - 1)
                battalion.append(1)
            elif battalion[i] == N:
                battalion.append(battalion[i] - 1)
                battalion.append(battalion[i+1])
                battalion.append(battalion[i])
                battalion.append(battalion[i+1] - 1)
                battalion.append(battalion[i])
                battalion.append(battalion[i+1] + 1)
            elif battalion[i+1] == M:
                battalion.append(battalion[i])
                battalion.append(battalion[i+1] - 1)
                battalion.append(battalion[i] + 1)
                battalion.append(battalion[i+1])
                battalion.append(battalion[i] - 1)
                battalion.append(battalion[i+1])
            else:
                battalion.append(battalion[i])
                battalion.append(battalion[i + 1] - 1)
                battalion.append(battalion[i])
                battalion.append(battalion[i + 1] + 1)
                battalion.append(battalion[i] - 1)
                battalion.append(battalion[i + 1])
                battalion.append(battalion[i] + 1)
                battalion.append(battalion[i + 1])
        delet.clear()
        for i in range(0, len(battalion), 2):
            if battalion[i] > N or battalion[i + 1] > M:
                delet.append(i)
            for j in range(i + 2, len(battalion), 2):
                if battalion[i] == battalion[j] and battalion[i + 1] == battalion[j + 1]:
                    delet.append(j)

        for d in delet:
            battalion[d] = 0
            battalion[d + 1] = 0
        while 0 in battalion:
            battalion.remove(0)

        day += 1
        am = L * 2
        L = len(battalion)
    return day
