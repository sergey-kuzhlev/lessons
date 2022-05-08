from typing import List

def MadMax(N: int, Tele: List[int]) -> int:
    """Sorts the array in ASC order, and then the right half in DESC order"""
    Tele = sorted(Tele)
    Tele_2 = sorted(Tele[(N - 1) // 2:], reverse=True)
    Tele[(N - 1) // 2:] = Tele_2

    return Tele
