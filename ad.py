print("hello")


bfs  dfs

# def main():

#     graph={
#     'a':['d','c'],
#     'b':['c'],
#     'c':['d'],
#     'd':['e'],
#     'e':['f'],
#     'f':[]

# }
#     visited=[]
#     visited1=[]
#     queue=[]
#     goal='f'

#     bfs(visited,graph,'a',queue)
#     print("dfs \n")
#     dfs(visited1,graph,'a')


# def bfs(visited,graph,node,queue):
#     visited.append(node)
#     queue.append(node)
#     while queue:
#         s=queue.pop(0)
#         print(s,end=" ")
#         for neighbour in graph[s]:
#             if neighbour not in visited:
#                 visited.append(neighbour)
#                 queue.append(neighbour)
#                 if neighbour=='d':
#                     break


# def dfs(visited,graph,node):
#     if node not in visited:
#         print(node , end=" ")
#         visited.append(node)
#         for neighbour in graph[node]:
#             dfs(visited,graph,neighbour)

# if __name__ == "__main__":
#     main()


n queen


# def isSafe(board,row,col,n):
#     for i in range(row):
#         if board[i][col]==1:
#             return False
        
#     i,j=row,col
#     while i>=0 and j>=0:
#         if board[i][j]==1:
#             return False
#         i-=1
#         j-=1

#     i,j=row,col
#     while i>=0 and j<n:
#         if board[i][j]==1:
#             return False
#         i-=1
#         j+=1

#     return True

# def solveNQueen(board,row,n):
#     if row>=n:
#         return True
    
#     i=0
#     while i<n:
#         if isSafe(board,row,i,n):
#             board[row][i]=1
#             if solveNQueen(board,row+1,n):
#                 return True
#             board[row][i]=0
#         i+=1

#     return False

# def print_board(board,n):
#     for i in range(n):
#         for j in range(n):
#             print(board[i][j],end=" ")
#         print()


# if __name__=="__main__":
#     n=7
#     board = [[0] * n for i in range(n)]

#     if solveNQueen(board,0,n):
#         print_board(board,n)
    
#     else:
#         print("No solution exists.")


Prims algorithm

# inf=99999999
# n=5

# g=[[8,2,3,4,5],
#    [5,4,3,2,7],
#    [6,4,3,7,5],
#    [9,3,5,7,9],
#    [2,4,6,8,0]]

# selected=[0,0,0,0,0]
# selected[0]=True
# no_edge=0
# while no_edge<n-1:
#     min=inf
#     a=0
#     b=0
#     for m in range(n):
#         if selected[m]:
#             for j in range(n):
#                 if (not selected[j] and g[m][j]):
#                     if min>g[m][j]:
#                         min=g[m][j]
#                         a=m
#                         b=j

#     print(str(a) + "-"+ str(b) +":"+str(g[a][b]))
#     selected[b]=True
#     no_edge+=1




A* Algorithm

# dict_hn={'A':10,'B':15,'C':20,'D':25,'E':30}
# dict_gn={
#     'A':{'B':10,'C':15,'D':14,'E':10},
#     'B':{'A':10,'C':15,'D':14,'E':10},
#     'C':{'B':10,'A':15,'D':14,'E':10},
#     'D':{'B':10,'C':15,'A':14,'E':10},
#     'E':{'B':10,'C':15,'D':14,'A':10},
# }

# start='A'
# goal='D'

# def getFn(citystr):
#     cities=citystr.split(',')
#     hn=dict_hn[cities[-1]]
#     gn=sum(dict_gn[cities[i]][cities[i+1]] for i in range(len(cities)-1))
#     return hn+gn

# def main():
#     cityq=[(getFn(start),start)]
#     while cityq:
#         total,citystr=cityq.pop(0)
#         thiscity=citystr.split(',')[-1]
#         if thiscity==goal:
#             result=citystr+'::'+str(total)
#             print("Result of A* is :-",result)
#             return
#         for i in  dict_gn[thiscity]:
#             cityq.append((getFn(citystr+','+i),citystr+','+i))
#         cityq.sort()

# main()

      
