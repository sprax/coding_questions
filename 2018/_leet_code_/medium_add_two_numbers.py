# https://leetcode.com/problems/add-two-numbers/description/

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.sum_inverted(l1, l2)
        
    def sum_inverted(self, n, p):
        carry = 0

        head = None
        previous = None

        while n or p:
            cur_sum = carry
            carry = 0

            if n:
                cur_sum += n.val
            if p:
                cur_sum += p.val

            if cur_sum >= 10:
               carry = 1 
               cur_sum -= 10

            node = ListNode(cur_sum)
            
            if previous:
                previous.next = node
                previous = previous.next
            else:
                head = node
                previous = node

            n = n.next if n else None
            p = p.next if p else None

        return head


###############################################################
import unittest

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def from_list(list):
    idx = 0
    while idx < len(list) - 1:
        list[idx].next = list[idx +1]
        idx += 1 
    return list[0]


def equals(l1, l2):
    if l1 is None and l2 is None:
        return True

    if l1 is None or l2 is None:
        return False

    if l1.val != l2.val:
        return False

    return equals(l1.next, l2.next)


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()
        n = [ListNode(1), ListNode(2), ListNode(3)]
        p = [ListNode(1), ListNode(9), ListNode(3)]
        res = [ListNode(2), ListNode(1), ListNode(7)]
        
        # 321 + 391 = 712
        self.assertTrue(equals(from_list(res),
                          s.addTwoNumbers(from_list(n), from_list(p))))

    def test_2(self):
        s = Solution()
        n = [ListNode(1), ListNode(2), ListNode(3)]
        p = [ListNode(4), ListNode(9)]
        res = [ListNode(5), ListNode(1), ListNode(4)]
        
        # 321 + 94 = 415
        self.assertTrue(equals(from_list(res),
                          s.addTwoNumbers(from_list(n), from_list(p))))


if __name__ == '__main__':
    unittest.main()