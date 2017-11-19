from random import randint

# def first_step():
#     lvlArray = [[] for i in range(20)]
#     for i in range(0, 20):
#         for j in range(0, 20):
#             if i == 0 or i == 19 or j == 0 or j == 19:
#                 lvlArray[i].append(1)
#             elif i > 0 and i < 19 and j > 0 and j < 19 and randint(0, 3) == 0:
#                 lvlArray[i].append(1)
#             else:
#                 lvlArray[i].append(0)
#     for i in range(1, 19):
#         for j in range(1, 19):
#             if ((lvlArray[i - 1][j] == 1 and lvlArray[i + 1][j] == 1 and lvlArray[i][j - 1] == 0 and lvlArray[i][
#                     j + 1] == 0) \
#                         or (lvlArray[i - 1][j] == 0 and lvlArray[i + 1][j] == 0 and lvlArray[i][j - 1] == 1 and lvlArray[i][
#                         j + 1] == 1)) \
#                     and (lvlArray[i - 1][j] != 2 and lvlArray[i + 1][j] != 2 and lvlArray[i][j - 1] != 2 and lvlArray[i][
#                             j + 1] != 2):
#                 if randint(0, 2) == 0:
#                     lvlArray[i][j] = 2
#                 else:
#                     lvlArray[i][j] = 0
#     lvlArray[1][1] = 3
#     return lvlArray
#
# def second_step(lvlArray):
#     for x in range(1, 19):
#         for y in range(1, 19):
#             if lvlArray[x][y]==3:
#                 if lvlArray[x-1][y]==0:
#                     lvlArray[x - 1][y]=3
#                 if lvlArray[x+1][y]==0:
#                     lvlArray[x + 1][y]=3
#                 if lvlArray[x][y-1]==0:
#                     lvlArray[x][y-1]=3
#                 if lvlArray[x][y+1]==0:
#                     lvlArray[x][y+1]=3
#                 if lvlArray[x-1][y]==2:
#                     lvlArray[x - 2][y]=3
#                 if lvlArray[x+1][y]==2:
#                     lvlArray[x + 2][y]=3
#                 if lvlArray[x][y-1]==2:
#                     lvlArray[x][y-2]=3
#                 if lvlArray[x][y+1]==2:
#                     lvlArray[x][y+2]=3
#     return lvlArray
#
# def third_step(lvlArray):
#     for x in range(1, 19):
#         for y in range(1, 19):
#             if lvlArray[x][y]==0:
#                 if x-1!=0 and lvlArray[x-1][y]==1:
#                     lvlArray[x-1][y]=0
#                 elif x+1!=19 and lvlArray[x+1][y]==1:
#                     lvlArray[x+1][y]=0
#                 elif y-1!=0 and lvlArray[x][y-1]==1:
#                     lvlArray[x][y-1]=0
#                 elif y+1!=19 and lvlArray[x][y+1]==1:
#                     lvlArray[x][y+1]=0
#     return lvlArray
#
# def fourth_step(lvlArray):
#     for i in range(0, 20):
#         for j in range(0, 20):
#             if i == 0 or i == 19 or j == 0 or j == 19:
#                 lvlArray[i].append(1)
#     return lvlArray

def generate_map():
    lvlArray= [[] for i in range(20)]
    for i in range(0, 20):
        for j in range(0, 20):
            if i == 0 or i == 19 or j == 0 or j == 19:
                lvlArray[i].append(1)
            else:
                lvlArray[i].append(0)
    X=[1,1]
    end=[18,18]
    lvlArray[X[0]][X[1]] = 3
    i=0
    while X!=end:
        Random=randint(0,2)
        if lvlArray[X[0]-1][X[1]]in[1,3] and lvlArray[X[0]+1][X[1]]in[1,3] and lvlArray[X[0]][X[1]+1]in[1,3]:
            X[1]+=1
        elif lvlArray[X[0]-1][X[1]]in[1,3] and lvlArray[X[0]+1][X[1]]in[1,3] and lvlArray[X[0]][X[1]-1]in[1,3]:
            X[1]-=1
        if lvlArray[X[0]-1][X[1]]in[1,3] and lvlArray[X[0]][X[1]-1]in[1,3] and lvlArray[X[0]][X[1]+1]in[1,3]:
            X[0]+=1
        elif lvlArray[X[0]+1][X[1]]in[1,3] and lvlArray[X[0]-1][X[1]]in[1,3] and lvlArray[X[0]][X[1]+1]in[1,3]:
            X[0]-=1
        elif lvlArray[X[0] - 1][X[1]] in [1, 3] and lvlArray[X[0]][X[1] - 1] in [1,3]:
            if Random==0:
                X[0]+=1
            else:
                X[1]+=1
        elif lvlArray[X[0] - 1][X[1]] in [1, 3] and lvlArray[X[0]][X[1] + 1] in [1, 3]:
            if Random==0:
                X[0]+=1
            else:
                X[1]-=1
        elif lvlArray[X[0] + 1][X[1]] in [1, 3] and lvlArray[X[0]][X[1] - 1] in [1,3]:
            if Random==0:
                X[0]-=1
            else:
                X[1]+=1
        elif lvlArray[X[0] + 1][X[1]] in [1, 3] and lvlArray[X[0]][X[1] + 1] in [1,3]:
            if Random==0:
                X[0]-=1
            else:
                X[1]-=1
        elif lvlArray[X[0] - 1][X[1]] in [1, 3] and lvlArray[X[0] + 1][X[1]] in [1,3]:
            if Random==0:
                X[1]-=1
            else:
                X[1]+=1
        elif lvlArray[X[0]][X[1] - 1] in [1, 3] and lvlArray[X[0]][X[1] + 1] in [1,3]:
            if Random==0:
                X[0]-=1
            else:
                X[0]+=1
        elif lvlArray[X[0] - 1][X[1]] in [1, 3]:
            if Random==0:
                X[1]+=1
            elif Random==1:
                X[1]-=1
            else:
                X[0]+=1
        elif lvlArray[X[0] + 1][X[1]] in [1, 3]:
            if Random == 0:
                X[1] += 1
            elif Random == 1:
                X[1] -= 1
            else:
                X[0] -= 1
        elif lvlArray[X[0]][X[1]-1] in [1, 3]:
            if Random == 0:
                X[0] += 1
            elif Random == 1:
                X[0] -= 1
            else:
                X[1] += 1
        elif lvlArray[X[0]][X[1]+1] in [1, 3]:
            if Random == 0:
                X[0] += 1
            elif Random == 1:
                X[0] -= 1
            else:
                X[1] -= 1
        lvlArray[X[0]][X[1]] = 3
        i += 1

    # lvlArray=first_step()
    # for x in range(0,10):
    #     lvlArray = second_step(lvlArray)
    # lvlArray = third_step(lvlArray)
    # lvlArray = second_step(lvlArray)
    # lvlArray = fourth_step(lvlArray)
    return lvlArray