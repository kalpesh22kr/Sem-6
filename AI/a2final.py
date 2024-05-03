class NQueens:
    def _init_(self):
        self.size = int(input("Enter size of Chessboard: "))
        if self.size == 0:
            print("Number of Solutions are : 0")
            return
        self.board = [[False] * self.size for _ in range(self.size)]
        self.count = 0

    def printBoard(self):
        for row in self.board:
            for ele in row:
                if ele == True:
                    print("Q", end=" ")
                else:
                    print("X", end=" ")
            print()
        print()

    def isSafe(self, row: int, col: int):
        for i in self.board:
            if i[col] == True:
                return False

        i = row
        j = col
        while i >= 0 and j >= 0:
            if self.board[i][j] == True:
                return False
            i -= 1
            j -= 1

        i = row
        j = col
        while i >= 0 and j < self.size:
            if self.board[i][j] == True:
                return False
            i -= 1
            j += 1

        return True

    def Solve(self, row: int):
        if row == self.size:
            self.count += 1
            self.printBoard()
            return

        for col in range(self.size):
            if self.isSafe(row, col):
                self.board[row][col] = True
                self.Solve(row + 1)
                self.board[row][col] = False


q = NQueens()
if q.size != 0:
    q.Solve(0)
    print("Number of Solutions are:", q.count)