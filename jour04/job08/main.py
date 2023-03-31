# from os.path import dirname, abspath, join


# f = open(join(dirname(abspath(__file__)), "..", "maze.mz"), "r")

# maze = f.read()
# maze = maze.splitlines()
# start_n = 0
# end = 0
# wall = "#"
# validePath = "."
# step = "X"



# def solveMaze(maze, x, y):
#     if maze[x][y] == validePath:
        
#     #    replace maze[x][y] with step
#         maze[x][y] = step
#         print(maze[4][0])
#         maze[x][y] = step
#         if x == len(maze) - 1 or y == len(maze[0]) - 1 or x == 0 or y == 0:
#             print(1)
#             return True
#         elif solveMaze(maze, x + 1, y) or solveMaze(maze, x - 1, y) or solveMaze(maze, x, y + 1) or solveMaze(maze, x, y - 1):
#             print(2)
#             return True
#         else:
#             maze[x][y] = validePath
#             print(3)
#             return False
#     else:
#         return False
    

    
        
# solveMaze(maze, 0, 0)


# # f2 = open('maze.out.mz.txt','w')
# # f2.write(maze)
# f.close()

from os.path import dirname, abspath, join

f = open(join(dirname(abspath(__file__)), "..", "maze.mz"), "r")
maze = f.read().splitlines()
start_n = 0
end = 0
wall = "#"
validePath = "."
step = "X"


def solveMaze(maze, x, y):
    if maze[x][y] == validePath:
        # Remplace maze[x][y] par step
        maze[x] = maze[x][:y] + step + maze[x][y+1:]
        # print(maze[4][0])
        if x == len(maze) - 1 or y == len(maze[0]) - 1 or x == 0 or y == 0:
            return True
        elif (solveMaze(maze, x + 1, y) or 
              solveMaze(maze, x - 1, y) or 
              solveMaze(maze, x, y + 1) or 
              solveMaze(maze, x, y - 1)):
            return True
        else:
            # Remet maze[x][y] à validePath si aucun chemin valide n'a été trouvé
            maze[x] = maze[x][:y] + validePath + maze[x][y+1:]
            return False
    else:
        return False

solveMaze(maze, 0, 0)

print(maze)
