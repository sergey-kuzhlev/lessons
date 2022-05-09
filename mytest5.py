from typing import List

def SynchronizingTables(N: int, ids: List[int], salary: List[int]) -> int:
    """returns the second array sorted by the first array"""
    db = {}
    ids_sort = sorted(ids)
    salary_sort = sorted(salary)
    for i in range(N):
        db.update({f'{ids_sort[i]}': f'{salary_sort[i]}'})
    for key, value in db.items():
        for i in range(N):
            if int(key) == ids[i]:
                salary[i] = int(value)

    return salary
