class Solution:
    def soln1(self, s: str, t: str) -> bool:
        def word_to_char_counts(word: str) -> dict[str, int]:
            result = {}
            for _, char in enumerate(word):
                if char not in result:
                        result[char] = 0
                result[char] = result[char] + 1
            return result
        return word_to_char_counts(s) == word_to_char_counts(t)


    def soln2(self, s: str, t: str) -> bool:
        return ''.join(sorted(s)) == ''.join(sorted(t))

    def isAnagram(self, s: str, t: str) -> bool:
        return self.soln1(s, t)

if __name__ == "__main__":
    soln = Solution()
    soln.soln1("ab","ba")

"""
Notes:

Solution 1:
Map of characters to counts. Compare maps for equality of both strings. time: O(n) space O(n)

Solution 2:
Sort then compare strings. Time: O(nlog(n)), space: O(1)

Stupid mistake, did not have the result[char] = result[char] + 1 in the loop

Note:
You can use python .get() function.
Familiarize yourself well with python data structures and functions
"""
