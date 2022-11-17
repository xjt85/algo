from typing import List, Tuple

list = [1, 2, 2, 3, 6, 7, 13, 15, 34, 45, 53, 55, 55, 56, 79, 134, 345]

def bin_search(i: int, lst: List[int]) -> List[int]:
    start_index = 0
    center_index = len(list) // 2
    finish_index = len(lst) - 1
    if lst[center_index] < i:
        start_index = center_index
    else:
        finish_index = center_index
