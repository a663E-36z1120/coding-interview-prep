from __future__ import annotations
from typing import *


class _Node:
    """A node in a linked list.

    Note that this is considered a "private class", one which is only meant
    to be used in this module by the LinkedList class, but not by client code.

    === Attributes ===
    item:
        The data stored in this node.
    next:
        The next node in the list, or None if there are no more nodes.
    """
    item: Any
    next: Optional[_Node]

    def __init__(self, item: Any) -> None:
        """Initialize a new node storing <item>, with no next node.
        """
        self.item = item
        self.next = None  # Initially pointing to nothing


class LinkedList:
    """A linked list implementation of the List ADT.
    """
    # === Private Attributes ===
    # _first:
    #     The first node in the linked list, or None if the list is empty.
    _first: Optional[_Node]

    def __init__(self, items: list) -> None:
        """Initialize a new linked list containing the given items.

        The first node in the linked list contains the first item
        in <items>.
        """
        if len(items) == 0:  # No items, and an empty list!
            self._first = None
        else:
            self._first = _Node(items[0])
            curr = self._first
            for item in items[1:]:
                curr.next = _Node(item)
                curr = curr.next

    def __str__(self) -> str:
        """Return a string representation of this list in the form
        '[item1 -> item2 -> ... -> item-n]'.

        >>> str(LinkedList([1, 2, 3]))
        '[1 -> 2 -> 3]'
        >>> str(LinkedList([]))
        '[]'
        """
        items = []
        curr = self._first
        while curr is not None:
            items.append(str(curr.item))
            curr = curr.next
        return '[' + ' -> '.join(items) + ']'

    def __len__(self) -> int:
        """Return the number of elements in this list.

        >>> lst = LinkedList([])
        >>> len(lst)              # Equivalent to lst.__len__()
        0
        >>> lst = LinkedList([1, 2, 3])
        >>> len(lst)
        3
        """
        curr = self._first
        count = 0
        while curr is not None:
            count += 1
            curr = curr.next
        return count

    def insert(self, index: int, item: Any) -> None:
        """Insert the given item at the given index in this list.
        Precondition: 0 <= index <= len(self)
        Note that adding to the end of the list is okay.
        >>> linky = LinkedList([1, 2, 3, 4])
        >>> linky.insert(0, 0)
        >>> str(linky)
        '[0 -> 1 -> 2 -> 3 -> 4]'
        >>> linky.insert(3, 2.5)
        >>> str(linky)
        '[0 -> 1 -> 2 -> 2.5 -> 3 -> 4]'
        """
        new_node = _Node(item)
        if index == 0:
            new_node.next = self._first  #
            self._first = new_node
        else:
            cur = self._first
            i = 0
            while cur is not None and i < index - 1:
                cur = cur.next
                i += 1
            new_node.next = cur.next
            cur.next = new_node  #

    def pop(self, index: int) -> Any:
        """Remove and return the item at position <index>.
        Precondition: 0 <= index < len(self)
        >>> lst = LinkedList([1, 2, 10, 200])
        >>> lst.pop(1)
        2
        >>> lst.pop(2)
        200
        >>> lst.pop(0)
        1
        """
        # pop the first node
        if index == 0:
            removed = self._first
            self._first = self._first.next
            return removed.item
        # pop another node
        else:
            cur = self._first
            i = 0
            while i < index - 1:
                cur = cur.next
                i += 1
            removed = cur.next
            cur.next = cur.next.next
            return removed.item

    def reverse_nodes(self, i: int) -> None:
        """Reverse the nodes at index i and i + 1 by changing their next references
        (not by changing their items).
        Precondition: Both i and i + 1 are valid indexes in the list.
        >>> lst = LinkedList([5, 10, 15, 20, 25, 30])
        >>> print(lst)
        [5 -> 10 -> 15 -> 20 -> 25 -> 30]
        >>> lst.reverse_nodes(1)
        >>> print(lst)
        [5 -> 15 -> 10 -> 20 -> 25 -> 30]
        >>> lst = LinkedList([5, 10, 15, 20, 25, 30])
        >>> lst.reverse_nodes(0)
        >>> print(lst)
        [10 -> 5 -> 15 -> 20 -> 25 -> 30]
        >>> lst = LinkedList([5, 10, 15, 20, 25, 30])
        >>> lst.reverse_nodes(4)
        >>> print(lst)
        [5 -> 10 -> 15 -> 20 -> 30 -> 25]
        """
        if i == 0:
            temp = self._first
            self._first = self._first.next
            temp.next = self._first.next
            self._first.next = temp
        else:
            curr = self._first
            for unused_ in range(i - 1):
                curr = curr.next
            temp = curr.next
            curr.next = curr.next.next
            temp.next = curr.next.next
            curr.next.next = temp

    def swap_halves(self) -> None:
        """Move the nodes in the second half of this list to the front.
        Precondition: len(self) >= 2
        >>> lst = LinkedList([5, 10, 15, 20, 25, 30])
        >>> print(lst)
        [5 -> 10 -> 15 -> 20 -> 25 -> 30]
        >>> lst.swap_halves()
        >>> print(lst)
        [20 -> 25 -> 30 -> 5 -> 10 -> 15]
        >>> lst = LinkedList([5, 10])
        >>> lst.swap_halves()
        >>> print(lst)
        [10 -> 5]
        >>> lst = LinkedList([5, 10, 15, 20, 25])
        >>> lst.swap_halves()
        >>> print(lst)
        [15 -> 20 -> 25 -> 5 -> 10]
        """
        # Compute the index of the node that will be the new first node.
        mid_index = len(self) // 2

        # Set first_end to refer to the node at the end of the first half
        first_end = self._first
        pos = 0
        while pos < mid_index - 1:
            first_end = first_end.next
            pos += 1

        # Set second_end to refer to the node at the end of the second half
        second_end = first_end.next
        while second_end.next is not None:
            second_end = second_end.next

        # Swap the halves
        second_end.next = self._first
        self._first = first_end.next
        first_end.next = None

    def average(self) -> float:
        """Return the average of the numbers in this linked list.
        Preconditions:
        - this linked list is not empty
        - all items in this linked list are numbers
        >>> lst = LinkedList([10, 15])
        >>> lst.average()
        12.5
        """
        curr = self._first
        counter = 0
        accumulator = 0

        while curr is not None:
            counter += 1
            accumulator += curr.item
            curr = curr.next

        return accumulator / counter

    def intersperse(self, other: LinkedList) -> None:
        """Insert the items of <other> in between the items of this linked list.
        Each item in <other> is inserted immediately after the corresponding item in <self>.
        Do not mutate <other> (this includes any of its nodes).
        See the doctest below for an example.
        Precondition: <self> and <other> have the same length.
        >>> lst1 = LinkedList([1, 2, 3])
        >>> lst2 = LinkedList([10, 20, 30])
        >>> str(lst1) # before
        '[1 -> 2 -> 3]'
        >>> lst1.intersperse(lst2)
        >>> str(lst1) # after
        '[1 -> 10 -> 2 -> 20 -> 3 -> 30]
        """
        curr1 = self._first
        curr2 = other._first

        # NOTE: You should do all of your work *inside* the while loop.
        # It is up to you to complete the while loop condition and its body.

        while curr1 is not None:
            new_node = _Node(curr2.item)
            new_node.next = curr1.next
            curr1.next = new_node
            curr1 = curr1.next.next
            curr2 = curr2.next

    def bisect(self, i: int) -> LinkedList:
        """Remove from this linked list the nodes at position i and beyond,
        and return them in a new linked list.
        The nodes in the new linked list should be in the same order as they
        were in <self>.
        Raise an IndexError if i < 0 or i >= the length of this linked list.
        Note: this is a mutating method because it modifies the contents
        of <self>.
        >>> linky1 = LinkedList([1, 2, 3, 4])
        >>> str(linky1)
        '[1 -> 2 -> 3 -> 4]'
        >>> str(linky1.bisect(0))
        '[1 -> 2 -> 3 -> 4]'
        >>> linky1._first is None
        True
        >>> linky2 = LinkedList([1, 2, 3, 4])
        >>> str(linky2.bisect(3))
        '[4]'
        >>> str(linky2.bisect(1))
        '[2 -> 3]'
        >>> str(linky2)
        '[1]'
        """
        if i < 0 or i >= self.__len__():
            raise IndexError
        elif i == 0:
            l = LinkedList([])
            l._first = self._first
            self._first = None
            return l
        else:
            index = 0
            curr = self._first
            while index < i - 1:
                curr = curr.next
                index += 1
            new_lst = LinkedList([])
            new_lst._first = curr.next
            curr.next = None
            return new_lst

    def do_stuff(self) -> None:
        """
        >>> lst = LinkedList([1, 2, 3, 10, 5, 6, 10, 8])
        >>> lst.do_stuff()
        >>> str(lst)
        '[1 -> 2 -> 10 -> 3 -> 5 -> 10 -> 6 -> 8]'
        """
        prev = self._first
        curr = self._first.next
        while curr is not None:
            if curr.item >= 10:
                curr.item, prev.item = prev.item, curr.item
            prev = curr
            curr = curr.next

    def insert_linked_list(self, other: LinkedList, pos: int) -> None:
        """Insert <other> into this linked list immediately before position
        pos.Do not make any new nodes, just link the existing nodes
        in.Preconditions:0 <= pos < len(self)len(other) >= 1
        >>> lst1 = LinkedList([0, 1, 2, 3, 4, 5])
        >>> lst2 = LinkedList([10, 11, 12])
        >>> lst1.insert_linked_list(lst2, 4)
        >>> str(lst1)
        '[0 -> 1 -> 2 -> 3 -> 10 -> 11 -> 12 -> 4 -> 5]'
        >>> lst3 = LinkedList([99])
        >>> lst1.insert_linked_list(lst3, 0)
        >>> str(lst1)
        '[99 -> 0 -> 1 -> 2 -> 3 -> 10 -> 11 -> 12 -> 4 -> 5]'
        """

        if pos == 0:
            last = other._first
            while last.next is not None:
                last = last.next
            last.next = self._first
            self._first = other._first
        else:
            curr = self._first
            for i in range(pos - 1):
                curr = curr.next

            last = other._first
            while last.next is not None:
                last = last.next

            last.next = curr.next
            curr.next = other._first


def swap(lst: LinkedList, i: int, j: int) -> None:
    """Swap the values stored at indexes <i> and <j> in the given linked list.
        Precondition: i and j are >= 0.
        Raise an IndexError if i or j (or both) are too large (out of bounds for this list).
        NOTE: You don't need to create new nodes or change any "next" attributes.
        You can implement this method simply by assigning to the "item" attribute of existing nodes.
        >>> linky = LinkedList([10, 20, 30, 40, 50])
        >>> swap(linky, 0, 3)
        >>> str(linky)
        '[40 -> 20 -> 30 -> 10 -> 50]'
        """
    index_i = 0
    curr_i = lst._first
    while index_i < i:
        if curr_i is not None:
            curr_i = curr_i.next
            index_i += 1
        else:
            raise IndexError

    index_j = 0
    curr_j = lst._first
    while index_j < j:
        if curr_j is not None:
            curr_j = curr_j.next
            index_j += 1
        else:
            raise IndexError

    curr_j.item, curr_i.item = curr_i.item, curr_j.item


class HoppingLinkedList(LinkedList):
    _refs: List[_Node]
    _k: int

    def __init__(self, k, items: list):
        LinkedList.__init__(self, items)
        self._k = k
        self._refs = [self._first]
        curr = self._first
        counter = 0
        while curr is not None:
            if counter % k == 0:
                self._refs.append(curr.next)
            counter += 1
            curr = curr.next




