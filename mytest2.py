def odometer(oksana: int) -> int:
    """
    the function of finding the way
    according to the array data
    """
    way = oksana[0] * (oksana[1])
    for i in range(2, len(oksana)):
        if i % 2 == 0:
            way += oksana[i] * (oksana[i + 1] - oksana[i - 1])
    return way
