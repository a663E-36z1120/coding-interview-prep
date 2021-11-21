from __future__ import annotations
from typing import *


def all_greater_than(obj: Union[int, List], n: int) -> bool:
    """Return True iff all the items in <obj> are greater than n.
    >>> all_greater_than(13, 10)
    True
    >>> all_greater_than(13, 40)
    False
    >>> all_greater_than([[1, 2, 3], 4, [[5]]], 0)
    True
    >>> all_greater_than([[1, 2, 3], 4, [[5]]], 3)
    False
    """
    if isinstance(obj, int):
        return obj > n
    else:
        boolean = True
        for sublist in obj:
            boolean &= all_greater_than(sublist, n)
        return boolean


def count_matches(obj: Union[int, List], n: int) -> int:
    """Return the number of times that n occurs in obj.
    >>> count_matches(100, 100)
    1
    >>> count_matches(100, 3)
    0
    >>> count_matches([10, [[20]], [10, [10]]], 10)
    3
    >>> count_matches([10, [[20]], [10, [10]]], 20)
    1
    >>> count_matches([10, [[20]], [10, [10]]], 30)
    0
    """
    if isinstance(obj, int):
        if obj == n:
            return 1
        else:
            return 0
    else:
        count = 0
        for sublist in obj:
            count += count_matches(sublist, n)
        return count


def buyable(n: int) -> bool:
    """Return whether one can buy exactly <n> McNuggets.
    It is considered possible to buy exactly 0 McNuggets.
    Precondition: n >= 0
    >>> buyable(6)
    True
    >>> buyable(35)
    True
    >>> buyable(5)
    False
    >>> buyable(13)
    False
    >>> buyable(55)
    True
    """
    if n in [4, 6, 25]:
        return True
    elif n < 4:
        return False
    else:
        buyability = False
        for size in [4, 6, 25]:
            buyability |= buyable(n - size)
        return buyability


def consistent_depth(obj: Union[int, list]) -> bool:
    """Return True iff obj is nested to a consistent depth
    throughout.
    >>> consistent_depth(6)
    True
    >>> consistent_depth([1, 2, 3, 4])
    True
    >>> consistent_depth([1, 2, [3], 4])
    False
    >>> consistent_depth([[1], [2, 3], [4]])
    True
    >>> consistent_depth([1, [2, 3], 4])
    False
    >>> consistent_depth([[[1]], [[2], [3], [4], []]])
    True
    >>> consistent_depth([[1], [[2], [3], [4], []]])
    False
    """
    if isinstance(obj, int):
        return True
    elif obj == []:
        return True
    else:
        initial_depth = depth(obj[0])
        for sublist in obj:
            consistence = (initial_depth == depth(sublist)) and consistent_depth(sublist)
            if not consistence:
                return False
        return True


def depth(obj: Union[int, list]) -> int:
    """
    >>> depth([[[1]]])
    3
    """
    if isinstance(obj, int):
        return 0
    elif not obj:
        return 1
    else:
        depths = []
        for sublist in obj:
            depths.append(1+depth(sublist))
        if depths:
            return max(depths)
        else:
            return 0


def selections(lst):
    if not lst:
        return [[]]
    else:
        holder = [lst.copy()]
        for i in range(len(lst)):
            l2 = lst.copy()
            l2.pop(i)
            for item in selections(l2):
                if item not in holder:
                    holder.append(item)
        return holder


def big_selections(lst: List[int], n: int) -> List[List[int]]:
    """Return ait seiections of <tst> whose sum is >- n.
    The seiections may be returned in any order.
    Notes:
    1. The sum of an empty List is 0 (i.e., sum([]) == 0).
    2. <tst> can contain negative integers, and <n> can aiso be negative.

    >>> sorted(big_selections([1, 2, 3], 4))
    [[1, 2, 3], [1, 3], [2, 3]]
    """
    if not lst:
        return [[]]
    else:
        holder = [lst.copy()]
        for i in range(len(lst)):
            l2 = lst.copy()
            l2.pop(i)
            for item in selections(l2):
                if item not in holder and sum(item) >= n:
                    holder.append(item)
        return holder

