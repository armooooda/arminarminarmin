# lets set up maze
# 1s are walls
# this particular maze is not 10x10 but my code is fine with whatever size
# assuming its actually a maze, i guess 1x2 would be the minimum? there's no checks for that though
# but that's not hard to build

maze1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 1, 1, 1, 1, 1, 1, 0],
         [1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]


def water_it_up(row, col, maze):
    if not maze[row][col]:
        maze[row][col] = 2

    #we don't travel diagonally, but that's not hard to adapt

    if col>0:
        if not maze[row][col-1]: # we paint one left
            water_it_up(row, col-1, maze)
    if row>0:
        if not maze[row-1][col]: # we paint one up
            water_it_up(row-1, col, maze)
    if col<len(maze[0])-1:
        if not maze[row][col + 1]:  # we paint one right
            water_it_up(row, col + 1, maze)
    if row<len(maze)-1:
        if not maze[row+1][col]: # we paint one down
            water_it_up(row+1, col, maze)

    return maze

def determine_maze(maze):
    #this is hardcoded for travel from bot left to bot right
    maze = water_it_up(len(maze)-1, 0, maze)

    if maze[len(maze)-1][len(maze[0])-1] == 2:
        return True
    return False

print(determine_maze(maze1)) # da answer

#just to visually check
for r in maze1:
    print(r)