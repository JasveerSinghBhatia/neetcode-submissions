class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        if len(t) > n:
            return ""

        mp = {}
        for ch in t:
            mp[ch] = mp.get(ch, 0) + 1

        req_cnt = len(t)

        i, j = 0, 0
        minwindow_size = float('inf')
        start_i = 0

        while j < n:
            ch = s[j]

            if mp.get(ch, 0) > 0:
                req_cnt -= 1

            mp[ch] = mp.get(ch, 0) - 1

            while req_cnt == 0:
                # shrink window
                currWindowSize = j - i + 1

                if minwindow_size > currWindowSize:
                    minwindow_size = currWindowSize
                    start_i = i

                mp[s[i]] = mp.get(s[i], 0) + 1

                if mp[s[i]] > 0:
                    req_cnt += 1

                i += 1

            j += 1

        return "" if minwindow_size == float('inf') else s[start_i:start_i + minwindow_size]