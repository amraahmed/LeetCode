# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above:


# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Example 2:
# Input: numRows = 1
# Output: [[1]]


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        root_list = []        
        for i in range(numRows+1):
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
        return root_list[1:]
            
            
            
#Runtime 36 ms Beats 63.81%
#Memory 13.9 MB Beats 62.10%
            
        