class NestedInteger(object):
    def __init__(self, val):
        self.val = val

    def isInteger(self):
        return isinstance(self.val, int)

    def getInteger(self):
        return self.val

    def getList(self):
        return self.val


from collections import namedtuple


class Entry:
    def __init__(self, cursor, iterator):
        self.cursor = cursor
        self.iterator = iterator


class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.iterator_stack = [Entry(cursor=-1, iterator=nestedList)]

    def next(self):
        """
        :rtype: int
        """
        next_i = self.iterator_stack[-1]
        res = next_i.iterator[next_i.cursor].getInteger()

        return res

    def hasNext(self):
        def wait_on_next():
            while len(self.iterator_stack) > 0:
                last = self.iterator_stack[-1]
                last.cursor += 1

                if last.cursor >= len(last.iterator):
                    self.iterator_stack.pop()
                    continue

                if last.iterator[last.cursor].isInteger():
                    return
                else:
                    self.iterator_stack.append(
                        Entry(-1, last.iterator[last.cursor].getList())
                    )

        wait_on_next()

        return len(self.iterator_stack) > 0


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        iterator = NestedIterator(
            [
                NestedInteger(1),
                NestedInteger([NestedInteger(2), NestedInteger([NestedInteger(3)])]),
                NestedInteger([NestedInteger(2), NestedInteger([NestedInteger(3)])]),
            ]
        )

        while iterator.hasNext():
            print(iterator.next())


if __name__ == "__main__":
    unittest.main(exit=False)
