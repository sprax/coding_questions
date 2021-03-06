from collections import deque

class PhoneDirectory:

    def __init__(self, maxNumbers):
        self._max_numbers = maxNumbers
        self._available = deque([n for n in range(maxNumbers)])
        self._used = set()
        

    def get(self):
        if len(self._available) == 0:
            return -1

        n = self._available.popleft()
        self._used.add(n)

        return n
        

    def check(self, number):
        return 0 <= number < self._max_numbers and number not in self._used;
        

    def release(self, number):
        if number not in self._used:
            return

        self._used.remove(number)
        self._available.appendleft(number)

        


###############################################################
import unittest

class TestFunctions(unittest.TestCase):
    def test_1(self):
        directory = PhoneDirectory(3)

        self.assertEqual(0, directory.get())
        self.assertEqual(1, directory.get())

        self.assertTrue(directory.check(2))
        self.assertEqual(2, directory.get())
        self.assertFalse(directory.check(2))

        directory.release(2)
        self.assertTrue(directory.check(2))

        directory.release(5)
        self.assertTrue(directory.check(2))
        self.assertFalse(directory.check(1))
        directory.release(1)

        self.assertTrue(directory.check(2))
        self.assertTrue(directory.check(1))


if __name__ == '__main__':
    unittest.main()