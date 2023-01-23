class Solution:
    def getRow(self, rowIndex: int) -> list[list[int]]:
        root_list = []        
        for i in range(rowIndex+2):
            lst=[1]            
            for x in range(1,i+1):
                try:
                    if x != i-1:
                        lst.append(root_list[i-1][x-1] +root_list[i-1][x])                 
                    else:
                        lst.append(1)                    
                except:
                    pass                                  
            root_list.append(lst)        
        root_list = root_list[1:]
        return root_list[-1]
    
    
sol =Solution()
print(sol.getRow(3))