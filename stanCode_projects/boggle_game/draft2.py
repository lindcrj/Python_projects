
class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def main():
    l1 = ListNode(2, None)
    l1.next = ListNode(4, None)
    l1.next.next = ListNode(3, None)
    traversal(l1)

    l2 = ListNode(5, None)
    l2.next = ListNode(6, None)
    l2.next.next = ListNode(4, None)
    traversal(l2)

    print('------------')

    ans = combine(l1, l2)
    traversal(ans)


def traversal(linked_list):
    cur = linked_list
    while linked_list.next is not None:
        print(linked_list.val, end='->')
        linked_list = linked_list.next
    print(linked_list.val)


def combine(l1, l2):
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

    # add_val = max_l.val + min_l.val
    # if plus == 1:
    #     add_val += 1
    #     plus = 0
    # if add_val > 9:
    #     add_val = add_val % 10
    #     plus = 1
    # ans_head = ListNode(add_val, None)
    # ans_cur = ans_head
    # max_l = max_l.next
    # min_l = min_l.next

    while max_l.next is not None:
        if min_l.next is not None:
            add_val = max_l.val + min_l.val
            if plus == 1:
                add_val += 1
                plus = 0
            if add_val > 9:
                add_val = add_val % 10
                plus = 1
            ans_head = ListNode(add_val, None)
            ans_cur = ans_head
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


    # cur = l1
    # curr = l2
    # len_l1 = 0
    # len_l2 = 0
    # plus = 0 #進位的開關
    #
    #
    #
    # # 記錄兩個linked list長度
    # if cur is not None:
    #     len_l1 += 1
    #     cur = cur.next
    #
    # if curr is not None:
    #     len_l2 += 1
    #     curr = curr.next
    #
    # # 比較兩者長度
    # if len_l1 > len_l2:
    #     max_l = l1
    #     min_l = l2
    #     cur = l1
    #     curr = l2
    # else:
    #     max_l = l2
    #     min_l = l1
    #     cur = l1
    #     curr = l2
    #
    # add_val = max_l.val + min_l.val
    # if plus == 1:
    #     add_val += 1
    #     plus = 0
    # if add_val > 9:
    #     add_val = add_val % 10
    #     plus = 1
    # ans_head = ListNode(add_val, None)
    # ans_cur = ans_head
    # max_l = max_l.next
    # min_l = min_l.next
    #
    # while max_l is not None:
    #     if min_l.next is not None:
    #         add_val = max_l.val + min_l.val
    #         if plus == 1:
    #             add_val += 1
    #             plus = 0
    #         if add_val > 9:
    #             add_val = add_val % 10
    #             plus = 1
    #         ans_head.next = ListNode(add_val, None)
    #         ans_head = ans_head.next
    #         max_l = max_l.next
    #         min_l = min_l.next
    #     else:
    #         min_l.next = ListNode(0, None)
    #         add_val = max_l.val + min_l.val
    #         if plus == 1:
    #             add_val += 1
    #             plus = 0
    #         if add_val > 9:
    #             add_val = add_val % 10
    #             plus = 1
    #         ans_head.next = ListNode(add_val, None)
    #         ans_head = ans_head.next
    #         max_l = max_l.next
    #         min_l = min_l.next
    # return ans_cur
    #
    #
    #































































if __name__ == "__main__":
    main()