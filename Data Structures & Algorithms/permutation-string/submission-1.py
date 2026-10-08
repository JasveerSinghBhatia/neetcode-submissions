class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n > m:
            return False

        sf1 = [0] * 26
        sf2 = [0] * 26

        # Frequency of characters in s1
        for ch in s1:
            sf1[ord(ch) - ord('a')] += 1

        i, j = 0, 0

        while j < m:
            # Add current character to window
            sf2[ord(s2[j]) - ord('a')] += 1

            # Maintain window size = n
            if j - i + 1 > n:
                sf2[ord(s2[i]) - ord('a')] -= 1
                i += 1

            # Check if current window is a permutation of s1
            if sf2 == sf1:
                return True

            j += 1

        return False