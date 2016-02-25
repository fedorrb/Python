def print_maze(maze,x,y):
    for i in range(len(maze)):
        s = ''
        for j in range(len(maze)):
            if i == x and j == y:
                s += 'X'
            elif maze[i][j] == 1:
                s += '1'
            else:
                s += '.'
        print s
    print ' '

class MazeRunner(object):

    def __init__(self, maze, start, finish):
        self.__maze = maze
        self.__rotation = (1,0)
        self.__x = start[0]
        self.__y = start[1]
        self.__finish = finish

    def go(self):
        x = self.__x + self.__rotation[0]
        y = self.__y + self.__rotation[1]
        if x > len(self.__maze)-1 \
            or y > len(self.__maze)-1 \
            or x < 0 or y < 0 \
            or self.__maze[x][y] == 1:
            return False
        self.__x = x
        self.__y = y
#        print_maze(self.__maze, self.__x, self.__y)
        return True

    def turn_left(self):
        left_rotation = {
            (0,1): (1,0),
            (1,0): (0,-1),
            (0,-1): (-1,0),
            (-1,0): (0,1),
        }
        self.__rotation = left_rotation[self.__rotation]
        return self

    def turn_right(self):
        right_rotation = {
            (1,0): (0,1),
            (0,-1): (1,0),
            (-1,0): (0,-1),
            (0,1): (-1,0),
        }
        self.__rotation = right_rotation[self.__rotation]
        return self

    def found(self):
        return self.__x == self.__finish[0] and self.__y == self.__finish[1]

def maze_controller(runner):
    #1
    def FourWay():
        i = 0
        arr = []
        while i < 4:
            i += 1
            while runner.go():
                if runner.found():
                    return
                arr.append(i)
            if len(arr):
                runner.turn_left()
                runner.turn_left()
                while len(arr):
                    arr.pop()
                    runner.go()
                runner.turn_left()
                runner.turn_left()
            runner.turn_left()

    def GoLeftSide(direct):
        runner.turn_left()
        d = 0
        if runner.go() == False:
            d = 2
            runner.turn_right()
            if runner.go() == False:
                d = 1
                runner.turn_right()
                if runner.go() == False:
                    d = 2
                    runner.turn_right()
                    runner.go()
        if d < 2:
            direct[d] += 1
        return direct

    def GoRightSide(direct):
        runner.turn_right()
        d = 0
        if runner.go() == False:
            d = 2
            runner.turn_left()
            if runner.go() == False:
                d = 1
                runner.turn_left()
                if runner.go() == False:
                    d = 2
                    runner.turn_left()
                    runner.go()
        if d < 2:
            direct[d] += 1
        return direct

    left_right = True
    direction = [0,0]
    i = 4
    counter = 0
    if runner.found() == False:
        while runner.found() == False:
            counter += 1
            if left_right or counter < 10000:
                direction = GoLeftSide(direction)
                FourWay()
                if (direction[0] > i) or (direction[1] > i):
                    direction[0] = 0
                    direction[1] = 0
                    left_right = False
                    while runner.go():
                        if runner.found():
                            break;
            else:
                direction = GoRightSide(direction)
                FourWay()
                if (direction[0] > i) or (direction[1] > i):
                    direction[0] = 0
                    direction[1] = 0
                    left_right = True
                    while runner.go():
                        if runner.found():
                            break;

    #2
##    import random
##    r = 0
##    if runner.found() == False:
##        while runner.found() == False:
##            r = random.randint(0,2)
##            if r == 0:
##                runner.go();
##            elif r == 1:
##                runner.turn_left()
##                runner.go()
##            else:
##                runner.turn_right();
##                runner.go()
    #3
##    def FourWay():
##        i = 0
##        while i < 4:
##            i += 1
##            while runner.go():
##                if runner.found():
##                    return
##                arr.append(i)
##            runner.turn_left()
##            runner.turn_left()
##            while len(arr):
##                arr.pop()
##                runner.go()
##
##    def GoLeftSide():
##        runner.turn_left()
##        if runner.go() == False:
##            runner.turn_right()
##            if runner.go() == False:
##                runner.turn_right()
##                if runner.go() == False:
##                    runner.turn_right()
##                    runner.go()
##
##
##
##    counter = 0
##    arr = []
##    if runner.found() == False:
##        while runner.found() == False:
##            GoLeftSide()
##            FourWay()



maze_example1 = {
    'm': [
        [0,1,0,0,0],
        [0,1,1,1,1],
        [0,0,0,0,0],
        [1,1,1,1,0],
        [0,0,0,1,0],
    ],
    's': (0,0),
    'f': (4,4)
}
maze_runner1 = MazeRunner(maze_example1['m'], maze_example1['s'], maze_example1['f'])
maze_controller(maze_runner1)
print maze_runner1.found()

maze_example2 = {
    'm': [
        [0,0,0,0,0,0,0,1],
        [0,1,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,0],
        [1,1,1,1,0,1,0,1],
        [0,0,0,0,0,1,0,1],
        [0,1,0,1,1,1,1,1],
        [1,1,0,0,0,0,0,0],
        [0,0,0,1,1,1,1,0],
    ],
    's': (7,7),
    'f': (0,0)
}
maze_runner2 = MazeRunner(maze_example2['m'], maze_example2['s'], maze_example2['f'])
maze_controller(maze_runner2)
print maze_runner2.found()   # True

maze_example3 = {
    'm': [
        [0,0,0,0,0,0,0,0,0,0,0],
        [1,0,1,1,1,0,1,1,1,0,1],
        [1,0,1,0,0,0,0,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,1,1,0,1,0,1],
        [1,0,1,0,0,0,0,0,1,0,1],
    ],
    's': (0,5),
    'f': (10,5)
}
maze_runner3 = MazeRunner(maze_example3['m'], maze_example3['s'], maze_example3['f'])
maze_controller(maze_runner3)
print maze_runner3.found()   # True

maze_example4 = {
    'm': [
        [0,0,0,0,1,0,1,0,0,0,0],
        [0,1,1,1,1,0,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,1,0,1,1,1,1,1,0,1,0],
        [1,1,0,1,0,0,0,1,0,1,1],
        [0,1,0,1,0,1,0,1,0,1,0],
        [0,1,0,0,0,1,0,0,0,1,0],
        [0,1,0,1,1,1,1,1,0,1,0],
        [0,1,0,0,0,0,0,0,0,1,0],
        [0,1,1,1,1,0,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0],
    ],
    's': (0,5),
    'f': (4,5)
}
maze_runner4 = MazeRunner(maze_example4['m'], maze_example4['s'], maze_example4['f'])
maze_controller(maze_runner4)
print maze_runner4.found()   # True

maze_example5 = {
    'm': [
        [0,0,0,1,1,0,1,1,0,0,0],
        [0,1,0,0,0,0,0,0,0,1,0],
        [0,1,0,1,1,1,1,1,0,1,0],
        [0,0,0,1,0,0,0,1,0,0,0],
        [0,0,1,1,0,0,0,1,1,0,0],
        [0,0,1,0,0,0,0,0,1,0,0],
        [0,0,1,0,1,0,1,0,1,0,0],
        [0,0,1,0,0,0,0,0,1,0,0],
        [0,0,1,1,1,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,0,1,0,1,0,1,0,0],
    ],
    's': (0,5),
    'f': (4,5)
}
maze_runner5 = MazeRunner(maze_example5['m'], maze_example5['s'], maze_example5['f'])
maze_controller(maze_runner5)
print maze_runner5.found()   # True