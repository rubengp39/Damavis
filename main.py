board = [4,3] # X, Y
snake = [[2,2],[3,2],[3,1],[3,0],[2,0],[1,0],[0,0]] # snake[0] = head --- Pop last and add new position to head.
depth = 3

# Assuming that movement will only be one in [L,R,U,D].
def nextState(board, snake, movement):
    if(movement == "L"):
        if(snake[0][0] > 0):
            snakeNextX = snake[0][0] + (-1)
            snakeNext = [snakeNextX, snake[0][1]]
            snake.pop()
            if((snakeNext not in snake)):
                snake.insert(0, snakeNext)
                return snake
            
    elif(movement == "R"):
        if(snake[0][0] < board[0]-1):
            snakeNextX = snake[0][0] + 1
            snakeNext = [snakeNextX, snake[0][1]]
            snake.pop()
            if((snakeNext not in snake)):
                snake.insert(0, snakeNext)
                return snake

    elif(movement == "U"):
        if(snake[0][1] > 0):
            snakeNextY = snake[0][1] + (-1)
            snakeNext = [snake[0][0], snakeNextY]
            snake.pop()
            if((snakeNext not in snake)):
                snake.insert(0, snakeNext)
                return snake

    elif(movement == "D"):
        if(snake[0][1] < board[1]-1):
            snakeNextY = snake[0][1] + 1
            snakeNext = [snake[0][0], snakeNextY]
            snake.pop()
            if((snakeNext not in snake)):
                snake.insert(0, snakeNext)
                return snake
    return None


def numberOfAvailableDifferentPaths(board, snake, depth):
    solution = 0
    snakeHead = snake[0]

    # Check Last depth possibilities recursively.
    

    return solution

print(nextState(board, snake, "U"))

