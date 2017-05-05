# variables
# m = The mouse's current location.
# c = This is where the mouse is trying to get to.
# o = A coordinate location that has NOT been checked.
# c = A coordinate point that has been checked.
# x = A barrier the mouse cannot travel through.

# EXPECTED RESULT: [(0,0), (0,1),(0,2),(1,2),(2,2),(3,2),(3,1)]
# CONSTRAINTS:

# this is a dictionary (Associative Array in python)
# coordMap = [(0, 0), (0, 1), (0, 2), (0, 3),
#            (1, 0), (1, 1), (1, 2), (1, 3),
#            (2, 0), (2, 1), (2, 2), (2, 3),
#            (3, 0), (3, 1), (3, 2), (3, 3)]

row1 = ["o", "o", "o", "o"]
row2 = ["m", "x", "o", "o"]
row3 = ["x", "x", "o", "o"]
row4 = ["c", "o", "o", "o"]

# M = the maze
M = [row1, row2, row3, row4]

# H = height of the maze
H = len(row1)

# W = width of the maze
W = len(M)




def ASearch(Maze):
    open, closed = [[mousePosition(Maze)]], [mousePosition(Maze)]
    # open is a list of paths, each of which begins at the mousePosition(M)
    # closed is a list of the cells we have found a shortest path to
    while len(open) > 0:
        path = open[0]
        destination = path[len(path) - 1]
        if Maze[destination[0]][destination[1]] == 'c':
            return path  # found the cheese
        open = open[1:]  # throw away the path we just tested       This was in the wrong place previously
        # insert children of path into open list. Each child is a path.
        for cell in adjacentCells(destination, Maze):
            if not cell in closed:
                open = insert(path+[cell], open, (3,0))
        open = open[1:]  # throw away the path we just tested
        closed = closed + [destination]
        return None


# ------------------------------------------------------------------------------------------------


def mousePosition(m):
    # mousePosition: maze -> cell
    # If M is a maze, mousePosition(M) is the position of the mouse in M.
    # If M is a maze and e is a pair of integers, then open(e,M)
    # iff e is a cell in M that doesn't contain 'x'
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 'm':
                return i, j


# ------------------------------------------------------------------------------------------------


def adjacentCells(c,m):
    # adjacentCells: cell*maze -> list<cell>
    # If c is a cell and M is a maze, adjacentCells(C,M) is a list of
    # the cells adjacent to C in M.

    # Two pairs (i,j) and (i',j') of integers are adjacent if i=i' and
    # |j-j'| = 1 or j=j' and |i-i'| =1.

    x, y = c
    c1, c2, c3, c4 = (x+1, y), (x-1, y), (x, y+1), (x, y-1)
    res = []
    for e in [c1, c2, c3, c4]:
        (i,j) = e
        maxi = len(m)-1
        maxj = len(m[0])-1
        if 0<i<=maxi and 0<j<=maxj and [i][j] in {'o', 'm', 'c'}:
            res = res+[e]
            return res


# ------------------------------------------------------------------------------------------------


# def insert(p, L, c):
    # insert: path * list<path>  * cell -> list<path>
    # If p is a path, L is a list of paths sorted in non decreasing
    # order by estimated total cost, and c is a cell,  then insert(p,L,c)
    # is the list obtained from L by inserting p so that the list
    # remains sorted. The estimated total cost of a path is its length
    # plus the manhattan distance from its last cell to c. For extra
    # credit, write this so that it runs in time O(log(len(L))).
#    ins = 1


#    return ins