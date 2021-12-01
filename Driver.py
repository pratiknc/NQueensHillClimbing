from NQueens import NQueens, FlatLocalMinimaException


def execNQueens(n, allowsidemove, sidemove, allowrandomrestart, failsteplist, successsteplist):
    '''
    Executes HillClimbing NQueens algorithm once.
    :param n: Number of queens
    :param allowsidemove: Boolean to allow or deny sideways move
    :param sidemove: Number of sidemoves allowed
    :param allowrandomrestart: Boolean to allow or deny random restart
    :param failsteplist: list storing number of steps for each failed hill-climbing
    :param successsteplist:  list storing number of steps for each succeeded hill-climbing
    '''
    if not allowsidemove and not allowrandomrestart:
        try:
            c = NQueens(n)
            c.execHillClimb()
            print('Succeeded in: ',c.getNumberOfMoves(),'moves')
            successsteplist.append(int(c.getNumberOfMoves()))
        except FlatLocalMinimaException as e:
            print("Local Minima Reached")
            print('Failed in: ',e.moves,'moves')
            failsteplist.append(int(c.getNumberOfMoves()))
            return
    if allowsidemove and not allowrandomrestart:
        try:
            c = NQueens(n, sidemove)
            # c = copy.deepcopy(c_rcv)
            c.execHillClimb()
            print('Succeeded in: ',c.getNumberOfMoves(),'moves')
            successsteplist.append(int(c.getNumberOfMoves()))
        except FlatLocalMinimaException as e:
            print("Exhausted Side Moves / ", e)
            print('Failed in: ',e.moves,'moves')
            failsteplist.append(int(c.getNumberOfMoves()))
            return

    if not allowsidemove and allowrandomrestart:
        move = 0
        while True:
            try:
                c = NQueens(n)
                c.execHillClimb()
                move = move+int(c.getNumberOfMoves())
                print('Succeeded in: ',move,'moves')
                successsteplist.append(move)
                break
            except FlatLocalMinimaException as e:
                print(e,' - Trying Random Restart')
                move = move+int(c.getNumberOfMoves())
                failsteplist.append(1)

    if allowsidemove and allowrandomrestart:
        move = 0
        while True:
            try:
                c = NQueens(n, sidemove)
                c.execHillClimb()
                move = move+int(c.getNumberOfMoves())
                print('Succeeded in: ',move,'moves')
                successsteplist.append(move)
                break
            except FlatLocalMinimaException as e:
                print("Exhausted Side Moves / ",e,' - Trying Random Restart')
                move = move+int(c.getNumberOfMoves())
                failsteplist.append(1)


n = int(input("Enter Number of Queens: ") or 5)
iterations = int(input("Enter Number of iterations: ") or 10)
allowsidemove = True if str(input("Allow Sideways Move ?(Y/N): ")).upper() == 'Y' else False
sidemove = int(input("Enter number of allowed side moves: ") or 100) if allowsidemove else 0
allowrandomrestart = True if str(input("Allow Random Restart ?(Y/N): ")).upper() == 'Y' else False
failsteplist = []
successsteplist = []


for i in range(0,iterations):
    execNQueens(n,allowsidemove,sidemove,allowrandomrestart,failsteplist,successsteplist)



if allowrandomrestart and not allowsidemove:
    print("Success Rate: ", len(successsteplist)//len(successsteplist)*100, '%')
    print("Average Number of Random Restarts without Side Ways move: ",sum(failsteplist)//len(failsteplist))
    print("Average Number of steps for Random Restarts without Side Ways move: ", sum(successsteplist)//len(successsteplist))
elif allowrandomrestart and allowsidemove:
    print("Success Rate: ", len(successsteplist)//len(successsteplist)*100, '%')
    print("Average Number of Random Restarts with Side Ways move: ",sum(failsteplist)//len(failsteplist))
    print("Average Number of steps for Random Restarts with Side Ways move: ", sum(successsteplist)//iterations)
elif not allowrandomrestart and allowsidemove:
    print("Success Rate: ", round((len(successsteplist)/iterations)*100), '%')
    print("Failure Rate: ", round(100-((len(successsteplist)/iterations)*100)), '%')
    print("Average number of steps on success with Side Ways move allowed: ", round(sum(successsteplist)/len(successsteplist)))
    print("Average number of steps on failure with Side Ways move allowed: ", round(sum(failsteplist)/len(failsteplist)))
elif not allowrandomrestart and not allowsidemove:
    print("Success Rate: ", (len(successsteplist)/iterations)*100, '%')
    print("Failure Rate: ", 100-((len(successsteplist)/iterations)*100), '%')
    print("Average number of steps on success: ", round(sum(successsteplist)/len(successsteplist)))
    print("Average number of steps on failure: ", round(sum(failsteplist)/len(failsteplist)))
