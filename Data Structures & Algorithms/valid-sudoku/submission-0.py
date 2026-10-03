class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        st = set()

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue

                row = board[i][j] + " ROW " + str(i)
                col = board[i][j] + " COL " + str(j)
                box = board[i][j] + " BOX " + str(i // 3) + "__" + str(j // 3)

                if row in st or col in st or box in st:
                    return False

                st.add(row)
                st.add(col)
                st.add(box)

        return True