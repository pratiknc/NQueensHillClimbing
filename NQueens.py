import random
import time


class FlatLocalMinimaException(Exception):
    '''
    Custom Exeption class. Denotes Flat Local minimum reached.
    '''
    def __init__(self, message, moves):
        self.moves = moves
        #Call the base class constructor with the parameters it needs
        super().__init__(message)


class NQueens:
    def random_state(self, n):
        """
        This will generate a random configuration of chess board with one queen in reach row.
        :param n: number of queens to place
        :return: Initial Board: Randomly generated board
                 QueenPos: Positions at which the queens are placed.
        """
        InitialBoard = [0 for i in range(0,n*n)]
        QueenPos = []

        for i in range (0, n*n , n):
            QueenPos.append(random.randint(i, i+n-1))
        for i in QueenPos:
            InitialBoard[i] = 1
        return InitialBoard, QueenPos

    def calculate_attack_vectors(self,fromPos,n):
        """
        This method will calculate positions a given queen can attack.
        :param fromPos: Queen position form which to calculate attacks.
               n: number of queens
        :return: list of all possible attacks from queens.
        """
        attack = [i for i in range(fromPos, n*n, n)]

        for i in range (0,n):
            LeftDiagonal = fromPos+((n-1)*i)
            RightDiagonal = fromPos+((n+1)*i)

            #check if end of the left diagonal is reached ??!! && check if end of the left diagonal is reached ??!!
            if int ( LeftDiagonal % n ) >= 0 and int ( LeftDiagonal % n ) < ( fromPos % n )  :             # and RightDiagonal< n*n
                if LeftDiagonal < n*n :#and LeftDiagonal != pos:
                    attack.append(LeftDiagonal)

            if int ( RightDiagonal % n ) <= n-1 and int ( RightDiagonal % n ) > (fromPos % n) :
                if RightDiagonal< n*n :
                    attack.append(RightDiagonal)

        return attack


    def printBoard(self,board):
        """
        This method will print given board as a n*n matrix.
        :param board: Input Board.
        """
        n = self.n
        i = 0
        j = n
        while j <= n*n:
            print(board[i : j])
            i = j
            j += n
        print()

    def calculateBoard(self,QueenPos,Board,UpdQueenPos = None):
        """
        This will calculate the heuristic cost on the board, which is the number of attacks performed for any given queen configuration.
        :param QueenPos: Current positions of queens, Board: Board on which to calculate heuristic
               ,UpdQueenPos: Optional, Will only update heuristics of these queens.
        :return: QueenAttacks: Number of attacks by each queen on queens below it.
        """
        if UpdQueenPos == None:
            UpdQueenPos = QueenPos
        queenAttackVectors = [self.calculate_attack_vectors(queen,self.n) for queen in QueenPos]
        QueenAttacks = self.QueenAttacks[:]
        for attack_vector in queenAttackVectors:
            queen_num = attack_vector.pop(0)//self.n
            attack_val = 0
            for pos in attack_vector:
                attack_val = Board[pos] + attack_val
            QueenAttacks[queen_num] = attack_val
        for pos in UpdQueenPos:
            self.Heuristic_board[pos] = sum(QueenAttacks)
        return QueenAttacks

    def moveQueen(self):
        """
        This will move the queen on calculation board to calculate the heuristic board.
        This does not move the queen on the output board.
        :param: N/A
        """
        for queen in range(0,self.n):
            for qpos in range(self.n*queen,self.n*(queen+1)):
                self.Calculation_board = self.InitialBoard.copy()
                QueenPos = self.QueenPos.copy()
                if qpos != self.QueenPos[queen]:
                    QueenPos[queen] = qpos
                    self.Calculation_board[self.QueenPos[queen]], self.Calculation_board[qpos] = self.Calculation_board[qpos], self.Calculation_board[self.QueenPos[queen]]
                    self.calculateBoard(QueenPos[0:queen+1], self.Calculation_board,QueenPos[queen:queen+1])
        self.Calculation_board = self.InitialBoard.copy()



    def getMovePos(self,min_heuristic):
        """
        This method the queen can be moved to based on minimum heuristic on the heuristic board :param minimum
        heuristic selected for movement.
        :return: position at which the queen should be moved, this position is
                selected randomly if more than one position with same heuristic cost are available
        """
        possible_moves = [i for i, x in enumerate(self.Heuristic_board) if x == min_heuristic]
        possible_moves = list((set(possible_moves) - set(self.QueenPos)) ) #- set([self.prevpos])
        random.seed(time.time())
        try:
            return random.choice(possible_moves)
        except:
            raise FlatLocalMinimaException('Flat Local min reached', self.getNumberOfMoves())

    def HillClimbMove(self,sidemove = 0):
        """
        This method performs hill climbing moves based on caldulated heuristics.
        :param sidemove: Number of side ways move allowed, defaulted to 0.
        :return: minimum heuristic cost which was chosen for moving the queen.
        """
        min_heuristic = min(self.Heuristic_board)
        if min_heuristic < self.prevMin:
            movepos = self.getMovePos(min_heuristic)
            queen = movepos//self.n
            self.InitialBoard[self.QueenPos[queen]], self.InitialBoard[movepos] = self.InitialBoard[movepos], self.InitialBoard[self.QueenPos[queen]]
            self.QueenPos[queen] = movepos
            self.Calculation_board = self.InitialBoard.copy()
            return min_heuristic, movepos
        elif self.allowed_size_move != 0 and min_heuristic == self.prevMin:
            movepos = self.getMovePos(min_heuristic)
            queen = movepos//self.n
            self.InitialBoard[self.QueenPos[queen]], self.InitialBoard[movepos] = self.InitialBoard[movepos], self.InitialBoard[self.QueenPos[queen]]
            self.QueenPos[queen] = movepos
            self.Calculation_board = self.InitialBoard.copy()
            self.allowed_size_move -= 1
            return min_heuristic, movepos
        else:
            raise FlatLocalMinimaException('Flat Local min reached', self.getNumberOfMoves())

    def getNumberOfMoves(self):
        """
        This method returns number of moves after problem success or failure.
        :param: N/A.
        :return: Number of moves performed by the hill-climbing algorithm.
        """
        return self.moves

    def execHillClimb(self):
        """
        This method executes hill climbing algorithm.
        :param: N/A.
        """
        print("\nQueens Moved as below\n")
        while True:
            self.QueenAttacks = self.calculateBoard(self.QueenPos,self.InitialBoard)
            if sum(self.QueenAttacks) == 0:
                break
            self.moveQueen()
            self.prevMin, self.prevpos = self.HillClimbMove(self.allowed_size_move)
            self.moves += 1
            self.printBoard(self.InitialBoard)


    def __init__(self, n, allowedsidemove = 0):
        """
        This method initializes the NQueens problem, with initial board and secondary boards for calculations.
        :param  n: Number of queens.
                allowedsidemove: Number of side moves allowed.
        """
        self.n = n
        self.allowed_size_move = allowedsidemove
        self.side_move = True if allowedsidemove != 0 else False
        self.moves = 0
        self.InitialBoard, self.QueenPos = self.random_state(n)
        self.Heuristic_board = [0 for i in range(0, n*n)]
        self.QueenAttacks = [n for i in range(0, n)]
        self.Calculation_board = self.InitialBoard.copy()
        self.prevMin = n*n
        self.prevpos = None
        print("\nInitial Board")
        self.printBoard(self.InitialBoard)



