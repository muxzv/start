from sys import setrecursionlimit

l= [
    [1,2,8], #line 1
    [3,4,7], #line 2
    [5,6,0] #line 3
    ]
    
def check(l,line,col):
    return line >= 0 and line < len(l) and col>=0 and col< len(l[0])

def path_fork(path):
    path_copy = path.copy()
    return path_copy

def rek(l,line,col,path):
    if not check(l,line,col):
        return
    # check cycle
    for el in path:
        line_i, col_i = el[0], el[1]
        if line == line_i and col == col_i:
            return
    path.append([line,col])
    print(path)
    rek(l,line-1,col,path_fork(path)) #вверх
    rek(l,line+1,col,path_fork(path)) #вниз
    rek(l,line,col+1,path_fork(path)) #вправо
    rek(l,line,col-1,path_fork(path)) #влево
    
setrecursionlimit(50)
path = []
rek(l,1,1,path)
