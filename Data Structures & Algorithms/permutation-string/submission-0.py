class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n > m:
            return False

        s1 = sorted(s1)

        for i in range(m - n + 1):
            substring = s2[i:i + n]
            substring = sorted(substring)

            if s1 == substring:
                return True

        return False