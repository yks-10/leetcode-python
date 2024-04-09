class Solution:
    def adjcentCheck(self, board1: list[list[str]], adjChar: str, row:int,col:int, result:dict) -> [bool,int,int]:
        adj = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        result = result
        for i in adj:
            r1,c1=i[0],i[1]
            try:
                if board1[row+r1][col+c1]==adjChar and (row+r1,col+c1) not in result:
                    return [True,row+r1,col+c1]
            except:
                continue
        else:
            return [False,row+r1,col+c1]

    def exist(self, board: list[list[str]], word: str) -> bool:
        if len(word)==len(board) and word==board[0]:
            return True
        result = {}
        length = len(board)
        initial = 0
        char = word[initial]
        row,col=0,0
        while row<length:
            l=board[row]
            while col<(len(l)):
                if l[col]==char:
                    adjChar = word[initial+1]
                    response = self.adjcentCheck(board,adjChar,row,col,result)
                    if response[0]==True and (row,col) not in result:
                        result[(row,col)]=char
                        row=response[1]
                        col=response[2]
                        char=adjChar
                        initial=initial+1
                        if len(result)==len(word)-1:
                            return True
                        break
                    else:
                        col += 1
                        continue
                else:
                    col+=1
            else:
                row+=1
                col=0
        else:
            return False


x = Solution()
print(x.exist([["a","a"]],"aaa"))