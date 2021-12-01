Code Instructions 
<br>Project name: N-Queens Problem with Hill Climbing and its variants.
<br>
<br>The project solved N-Queens Problem using Hill Climbing and its variants.
<br>
<br>1. Hill Climbing – Steepest Ascent – Try to solve N-Queens problem by starting from a random 
<br>start state and moving to a better state. This will fail in case we can’t find a state better than current 
<br>state.
<br>2. Hill Climbing – With Sideways Move – Works same as Hill Climbing – Steepest Ascent, 
<br>however, when we cannot find a state with better heuristic cost, we still make a move if a state with 
<br>same heuristic cost as current state exists, we do this till we either find a better state or exhaust a predetermined quota of such same heuristic cost moves.
<br>3. Hill Climbing – With Random Restart – Works same as Hill Climbing – Steepest Ascent, 
<br>however, when we cannot find a state with better heuristic cost, we abandon the current search and 
<br>start with a random initial state. This is repeated till solution is found.
<br>4. Hill Climbing – With Random Restart – This is a combination of all the above three approaches, 
<br>where if we cannot find a state with better heuristic cost, we still make a move if a state with same 
<br>heuristic cost as current state exists, we do this till we either find a better state or exhaust a pre-determined quota of such same heuristic cost moves. Upon reaching this state, we abandon the current 
<br>search and start with a random initial state. This is repeated till solution is found.
<br>
<br>The driver file expects the following as input –
<br>1. Number of queens – The number of queens to run the problem for. 
<br>2. Number of iterations – Number of iterations to run the problem for. Default value is set to 10.
<br>3. Allow sideways move (Y/N) - Whether sideways moves are allowed or not.
<br>4. Number of sideways moves allowed– If sideways moves are allowed, the maximum number of such moves.
<br>5. Allow Random restart (Y/N) - Whether Random restart is allowed or not.
<br>
<br>Prerequisites: 
<br>Before you begin, ensure you have met the following requirements: 
<br>• You have installed Python version 3.7+
<br>All Operating Systems are supported. 
<br>Usage: 
<br>1. Extract the zip file on desired path. 
<br>2. Navigate to src folder. 
<br>3. Run Driver.py –
<br>python Driver.py 
<br>
<br>On execution, follow the prompts –
<br>"Enter Number of Queens:" – The number of queens to run the problem for.
<br>"Enter Number of iterations: " – Number of iterations to execute the problem for.
<br>"Allow Sideways Move ?(Y/N):” – “Y” if sideways moves are allowed, “N” otherwise. Defaulted to “N”
<br>"Enter number of allowed side moves:" – If sideways moves are allowed, limit on sideways move. 
<br>Defaulted to 100
<br>"Allow Random Restart Move ?(Y/N):” – “Y” if random restarts are allowed, “N” otherwise. Defaulted 
<br>to “N”
<br>
<br>The program will then print step sequence under execution.
<br>Example – “<Path to File>/Driver.py”
<br>Enter Number of Queens: 8
<br>Enter Number of iterations: 100
<br>Allow Sideways Move ?(Y/N): N
<br>Allow Random Restart ?(Y/N): N
