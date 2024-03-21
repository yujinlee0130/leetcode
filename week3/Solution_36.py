class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        mydict = defaultdict(list) # list of tuples 
        for i in range(9): 
            for j in range(9):
                elt = board[i][j]
                if elt != ".":
                    if elt in mydict:
                        for pos in mydict[elt]:  # position list [(0,0), (1,1)]
                            if i == pos[0] or j == pos[1] or (i//3 == pos[0]//3 and j//3 == pos[1]//3):
                                print(i, pos[0])
                                print(j, pos[1])
                                print(i//3, pos[0])
                                print(j//3, pos[1])
                                return False

                    #add to set
                    mydict[elt].append((i,j))
        return True
                    
                