class Solution:
    def operate(self, a, b, token) -> int:
        if token == '+':
            return a + b
        elif token == '-':
            return a - b
        elif token == '*':
            return a * b
        else:
            return int(a / b)

    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for token in tokens:
            if token == '+' or token == '-' or token == '*' or token == '/':
                b = st[-1]
                st.pop()

                a = st[-1]
                st.pop()

                result = self.operate(a, b, token)
                st.append(result)
            else:
                st.append(int(token))

        return st[-1]