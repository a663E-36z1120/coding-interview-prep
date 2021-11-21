from __future__ import annotations
from typing import Any, Dict, List, Optional


class BinarySearchTree:
    """Binary Search Tree class.

    This class represents a binary tree satisfying the Binary Search Tree
    property: for every item, its value is >= all items stored in its left
    subtree, and <= all items stored in its right subtree.
    """
    # === Private Attributes ===
    # The item stored at the root of the tree, or None if the tree is empty.
    _root: Optional[Any]
    # The left subtree, or None if the tree is empty.
    _left: Optional[BinarySearchTree]
    # The right subtree, or None if the tree is empty.
    _right: Optional[BinarySearchTree]

    # === Representation Invariants ===
    #  - If self._root is None, then so are self._left and self._right.
    #    This represents an empty BST.
    #  - If self._root is not None, then self._left and self._right
    #    are BinarySearchTrees.
    #  - (BST Property) If self is not empty, then
    #    all items in self._left are <= self._root, and
    #    all items in self._right are >= self._root.

    def __init__(self, root: Optional[Any]) -> None:
        """Initialize a new BST containing only the given root value.

        If <root> is None, initialize an empty tree.
        """
        if root is None:
            self._root = None
            self._left = None
            self._right = None
        else:
            self._root = root
            self._left = BinarySearchTree(None)
            self._right = BinarySearchTree(None)

    def is_empty(self) -> bool:
        """Return whether this BST is empty.

        >>> bst = BinarySearchTree(None)
        >>> bst.is_empty()
        True
        >>> bst = BinarySearchTree(10)
        >>> bst.is_empty()
        False
        """
        return self._root is None

    # -------------------------------------------------------------------------
    # Standard Container methods (search, insert, delete)
    # -------------------------------------------------------------------------
    def __contains__(self, item: Any) -> bool:
        """Return whether <item> is in this BST.

        >>> bst = BinarySearchTree(3)
        >>> bst._left = BinarySearchTree(2)
        >>> bst._right = BinarySearchTree(5)
        >>> 3 in bst
        True
        >>> 5 in bst
        True
        >>> 2 in bst
        True
        >>> 4 in bst
        False
        """
        if self.is_empty():
            return False
        elif item == self._root:
            return True
        elif item < self._root:
            return item in self._left  # or, self._left.__contains__(item)
        else:
            return item in self._right  # or, self._right.__contains__(item)

    def __str__(self) -> str:
        """Return a string representation of this BST.

        This string uses indentation to show depth.
        """
        return self._str_indented(0)

    def _str_indented(self, depth: int) -> str:
        """Return an indented string representation of this BST.

        The indentation level is specified by the <depth> parameter.
        """
        if self.is_empty():
            return depth * '  ' + '-\n'
        else:
            answer = depth * '  ' + str(self._root) + '\n'
            if not (self._left.is_empty() and self._right.is_empty()):
                answer += self._left._str_indented(depth + 1)
                answer += self._right._str_indented(depth + 1)
            return answer

    def insert(self, item: Any) -> None:
        """Insert <item> into this BST, maintaining the BST property.

        Do not change positions of any other nodes.

        >>> bst = BinarySearchTree(10)
        >>> bst.insert(3)
        >>> bst.insert(20)
        >>> bst._root
        10
        >>> bst._left._root
        3
        >>> bst._right._root
        20
        """
        if self.is_empty():
            self._root = item
            self._left, self._right = BinarySearchTree(None), \
                                      BinarySearchTree(None)
        else:
            if item <= self._root:
                self._left.insert(item)
            else:
                self._right.insert(item)

    def items(self) -> List:
        """Return all of the items in the BST in sorted order.

        You should *not* need to sort the list yourself: instead, use the BST
        property and combine self._left.items() and self._right.items()
        in the right order!

        >>> BinarySearchTree(None).items()  # An empty BST
        []
        >>> bst = BinarySearchTree(7)
        >>> bst.items()
        [7]
        >>> left = BinarySearchTree(3)
        >>> left._left = BinarySearchTree(2)
        >>> left._right = BinarySearchTree(5)
        >>> right = BinarySearchTree(11)
        >>> right._left = BinarySearchTree(9)
        >>> right._right = BinarySearchTree(13)
        >>> bst._left = left
        >>> bst._right = right
        >>> bst.items()
        [2, 3, 5, 7, 9, 11, 13]
        """
        if self.is_empty():
            return []
        else:
            llst = self._left.items()
            rlst = self._right.items()
            llst.append(self._root)
            llst.extend(rlst)
            return llst

    def verify(self) -> bool:
        """Verify that the bst structure is intact.
        >>> bst = BinarySearchTree(3)
        >>> bst._left = BinarySearchTree(2)
        >>> bst._right = BinarySearchTree(5)
        >>> bst._right._right = BinarySearchTree(5)
        >>> bst._right._left = BinarySearchTree(4)
        >>> bst.verify()
        True
        >>> bst = BinarySearchTree(8)
        >>> bst._left = BinarySearchTree(2)
        >>> bst._right = BinarySearchTree(5)
        >>> bst.verify()
        False
        >>> bst = BinarySearchTree(3)
        >>> bst._left = BinarySearchTree(2)
        >>> bst._right = BinarySearchTree(5)
        >>> bst._right._right = BinarySearchTree(5)
        >>> bst._right._left = BinarySearchTree(6)
        >>> bst.verify()
        False
        """
        if self.is_empty():
            return True
        else:
            left_list, right_list = self._left.items(), self._right.items()
            if self._left.verify() and self._right.verify():
                for item in left_list:
                    if item > self._root:
                        return False
                for item in right_list:
                    if item < self._root:
                        return False
                return True
            else:
                return False

    def height(self) -> int:
        if self.is_empty():
            return 0
        else:
            return 1 + max(self._left.height(), self._right.height())

    def items_in_range(self, start: Any, end: Any) -> List:
        """Return the items in this BST between <start> and <end>, inclusive.
        Precondition: att items in this BST can be compared with <start> and <end>.
        'The items should be returned in sorted order, but do *not* use the built-in
        List.sort
        or sorted functions.

        >>> bst = make_bst([7, 6, 4, 0, 1, 8, 5, 6, 5, 9, 1, 2, 5, 7])
        >>> lst = [7, 6, 4, 0, 1, 8, 5, 6, 5, 9, 1, 2, 5, 7]
        >>> lst.sort()
        >>> bst.items_in_range(0, 9) == lst
        True
        >>> bst = make_bst([7, 6, 4, 0, 1, 8, 5, 6, 5, 9, 1, 2, 5, 7])
        >>> bst.items_in_range(0, 2)
        [0, 1, 1, 2]
        """
        if self.is_empty():
            return []
        else:
            left = self._left.items_in_range(start, end)
            right = self._right.items_in_range(start, end)
            mid = []
            if start <= self._root <= end:
                mid = [self._root]
            return left + mid + right

    def distribution(self) -> Dict:
        """
        >>> bst = BinarySearchTree(None)
        >>> bst.insert(39)
        >>> bst.insert(39)
        >>> bst.insert(-4)
        >>> bst.insert(39)
        >>> bst.insert(105)
        >>> bst.insert(-4)
        >>> bst.distribution() == {39: 3, -4: 2, 105: 1}
        True
        """
        if self.is_empty():
            return {}
        else:
            dct = {self._root: 1}
            absorb(dct, self._right.distribution())
            absorb(dct, self._left.distribution())
            return dct

    def levels(self) -> List:
        if self.is_empty():
            return []
        # elif self._left.is_empty() and self._right.is_empty():
        #     return [(1, [self._root])]
        else:
            lst = [(1, [self._root])]
            left_levels = self._left.levels()
            right_levels = self._right.levels()
            if len(left_levels) > len(right_levels):
                sublevels = left_levels
            else:
                sublevels = right_levels
            for i in range(len(sublevels)):
                if i < len(left_levels) and i < len(right_levels):
                    new_lst = left_levels[i][1]
                    new_lst.extend(right_levels[i][1])
                    new_tuple = (sublevels[i][0] + 1,
                                 new_lst)
                else:
                    new_tuple = sublevels[i]
                lst.append(new_tuple)
            return lst

    def eggplant(self):
        if not self.is_empty():
            if not self._left.is_empty() and not self._right.is_empty():
                self._root = self._left._root + self._right._root
                self._left.eggplant()
                self._right.eggplant()

def make_bst(lst: List[int]) -> BinarySearchTree:
    """Make a binary search tree with the given list.
    >>> bst = make_bst([7, 6, 4, 0, 1, 8, 5, 6, 5, 9, 1, 2, 5, 7])
    >>> bst.verify()
    True
    """
    lst = lst.copy()
    bst = BinarySearchTree(None)
    for item in lst:
        bst.insert(item)
    return bst


def absorb(d1: dict, d2: dict) -> None:
    for item in d2:
        if item in d1:
            d1[item] += d2[item]
        else:
            d1[item] = d2[item]




################################################################################
# December 2018
################################################################################

# (c) [2 marks] Suppose we have an empty BST, and want to insert the values 1
# to 6 (inclusive), in some order, using the insertion algorithm covered in
# this course. If we insert the values in the order [ 1, 2, 3, 4, 5, 6] or [
# 6, 5, 4, 3, 2, 1] , we would obtain a BST of height 6. (i) Write down
# another order (different from the above two) we could insert the values 1-6
# into an empty BST to obtain a BST of height 6. (ii) Draw the BST that would
# result if we inserted the values in this order.

# [6, 1, 5, 2, 4, 3]

# 6
#     1
#         -
#         5
#             2
#                 -
#                 4
#                     3
#                     -
#             -
#     -











