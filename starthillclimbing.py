import random

def show_board(board):
    for row in board:
        print(' '.join(str(cell) for cell in row))
    print()

def find_heuristic(board):
    n = len(board)
    get_conflicts = 0
    for i in range(n):
     for j in range(n):
         if board[i][j] == 1:
             for k in range(1, n):

                    if i + k < n and board[i + k][j] == 1:
                            get_conflicts += 1
                    if j + k < n and board[i][j + k] == 1:

                        get_conflicts += 1
                    if i + k < n and j + k < n and board[i + k][j + k] == 1:

                            get_conflicts += 1
                    if i - k >= 0 and j + k < n and board[i - k][j + k] == 1:

                        get_conflicts += 1
    return get_conflicts





def switch_random_board(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    for col in range(n):
        row = random.randint(0, n - 1)
        
        board[row][col] = 1

    return board





def find_neighbors(board):
    n = len(board)
    neighbors = []
    for col in range(n):

        for row in range(n):

          if board[row][col] == 1:

                for new_row in range(n):

                 if new_row != row:
                        new_board = [list(r) for r in board]
                       
                        new_board[row][col] = 0
                        new_board[new_row][col] = 1
                     
                        neighbors.append(new_board)

    return neighbors




def start_hill_climbing(n):
    restarts = 0
    total_changes = 0

    while True:
        present_board = switch_random_board(n)
        present_heuristic = find_heuristic(present_board)

        while True:
            show_board(present_board)
            print("Current heuristic:", present_heuristic)

            neighbors = find_neighbors(present_board)
            next_board = None

            next_heuristic = present_heuristic


            for neighbor in neighbors:
                h = find_heuristic(neighbor)

                if h < next_heuristic:
                    next_board = neighbor

                
                    next_heuristic = h



            if next_heuristic >= present_heuristic:
                print("Random restart\n")

                restarts += 1
                break
            else:
                present_board = next_board
                
                present_heuristic = next_heuristic

                total_changes += 1

            print("Total state changes:", total_changes)



        if present_heuristic == 0:
            
            print("Solution found")
            show_board(present_board)
            
            print("Total restarts:", restarts)
            
            print("Total state changes:", total_changes)
            return present_board

n = 8
start_hill_climbing(n)
