from collections import defaultdict, deque
from heapq import heappush, heappop


class Solution:
    def alienOrder2(self, words):
        indegree = defaultdict(int)
        dependencies = defaultdict(set)

        for i in range(len(words)):
            for letter in list(words[i]):
                if letter not in indegree:
                    indegree[letter] = 0

            for j in range(i + 1, len(words)):
                i_idx = j_idx = 0
                while i_idx < len(words[i]) and j_idx < len(words[j]):
                    before = words[i][i_idx]
                    after = words[j][j_idx]

                    if before != after:
                        if after in dependencies and before in dependencies[after]:
                            return ""

                        if (
                            before not in dependencies
                            or after not in dependencies[before]
                        ):
                            dependencies[before].add(after)
                            indegree[after] += 1
                        break

                    i_idx += 1
                    j_idx += 1

        queue = deque()
        for letter, degree in indegree.items():
            if degree == 0:
                queue.append(letter)

        ans = []
        while len(queue) > 0:
            next_letter = queue.popleft()
            ans.append(next_letter)

            for neighbor in dependencies[next_letter]:
                if indegree[neighbor] > 0:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)

        return "".join(ans)

    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        iam_bigger_than = defaultdict(set)
        known_letters = set()

        for i in range(len(words)):
            known_letters.update(list(words[i]))
            for j in range(i + 1, len(words)):
                i_idx = j_idx = 0
                while i_idx < len(words[i]) and j_idx < len(words[j]):
                    before = words[i][i_idx]
                    after = words[j][j_idx]

                    if before != after:
                        if (
                            before in iam_bigger_than
                            and after in iam_bigger_than[before]
                        ):
                            return ""

                        iam_bigger_than[after].add(before)
                        break

                    i_idx += 1
                    j_idx += 1

        visited = set()

        def expand(letter):
            nonlocal iam_bigger_than, visited

            if letter in visited:
                return iam_bigger_than[letter]

            visited.add(letter)

            for smaller in [l for l in iam_bigger_than[letter]]:
                iam_bigger_than[letter].update(expand(smaller))

            return iam_bigger_than[letter]

        heap = []
        for letter in known_letters:
            expand(letter)
            heappush(heap, (len(iam_bigger_than[letter]), letter))

        ans = []
        while len(heap) > 0:
            ans.append(heappop(heap)[1])

        return "".join(ans)


###############################################################
import unittest


class TestFunctions(unittest.TestCase):
    def test_1(self):
        s = Solution()

        self.assertEqual("wertf", s.alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))
        self.assertEqual("zx", s.alienOrder(["z", "x"]))
        self.assertEqual("", s.alienOrder(["z", "x", "z"]))
        self.assertEqual("abcd", s.alienOrder(["ab", "adc"]))

        self.assertEqual("wertf", s.alienOrder2(["wrt", "wrf", "er", "ett", "rftt"]))
        self.assertEqual("zx", s.alienOrder2(["z", "x"]))
        self.assertEqual("", s.alienOrder2(["z", "x", "z"]))
        self.assertEqual("abcd", s.alienOrder2(["ab", "adc"]))


if __name__ == "__main__":
    unittest.main()
