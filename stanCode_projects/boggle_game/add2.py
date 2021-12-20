"""
File: add2.py
Name:
------------------------
TODO:
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    #######################
    #                     #
    #        TODO:        #
    #                     #
    #######################
    cur = l1
    curr = l2
    len_l1 = 0
    len_l2 = 0
    plus = 0  # 進位的開關

    while cur is not None:
        len_l1 += 1
        cur = cur.next

    while curr is not None:
        len_l2 += 1
        curr = curr.next

    # 比較兩者長度
    if len_l1 > len_l2:
        max_l = l1
        min_l = l2

    else:
        max_l = l2
        min_l = l1

    add_val = max_l.val + min_l.val
    if plus == 1:
        add_val += 1
        plus = 0
    if add_val > 9:
        add_val = add_val % 10
        plus = 1
    ans_head = ListNode(add_val, None)
    ans_cur = ans_head
    if max_l.next is None:
        return ans_cur
    else:
        max_l = max_l.next
        min_l = min_l.next

        while max_l.next is not None:
            if min_l.next is not None:
                add_val = max_l.val + min_l.val
                if plus == 1:
                    add_val += 1
                    plus = 0
                if add_val > 9:
                    add_val = add_val % 10
                    plus = 1
                ans_head.next = ListNode(add_val, None)
                ans_head = ans_head.next
                max_l = max_l.next
                min_l = min_l.next
            else:
                min_l.next = ListNode(1, None)
                min_l.next.val -= 1
                add_val = max_l.val + min_l.val
                if plus == 1:
                    add_val += 1
                    plus = 0
                if add_val > 9:
                    add_val = add_val % 10
                    plus = 1
                ans_head.next = ListNode(add_val, None)
                ans_head = ans_head.next
                max_l = max_l.next
                min_l = min_l.next
        add_val = max_l.val + min_l.val
        if plus == 1:
            add_val += 1
            plus = 0
        if add_val > 9:
            add_val = add_val % 10
            plus = 1
        ans_head.next = ListNode(add_val, None)
        ans_head = ans_head.next

        if plus == 1:
            ans_head.next = ListNode(1, None)

        return ans_cur


####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
