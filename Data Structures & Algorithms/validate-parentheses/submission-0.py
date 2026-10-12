class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for ch in s:
            if not st or ch == '(' or ch == '[' or ch == '{':
                st.append(ch)
                continue

            if ch == ')':
                if st[-1] == '(':
                    st.pop()
                else:
                    return False

            elif ch == ']':
                if st[-1] == '[':
                    st.pop()
                else:
                    return False

            elif ch == '}':
                if st[-1] == '{':
                    st.pop()
                else:
                    return False

        return len(st) == 0