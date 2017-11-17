class Solution:
    def plusOne(self, A):
            res = []
            added = False

            if not A: 
                return [1]
            
            if len(A) ==1 and A[0]==0:
                return [1]
                
            while A and not A[0]:
                A = A[1:]
            
            for i in range(1, len(A)+1):
                if A[-i] == 9 and not added:
                    res.append(0)
                    if i == len(A):
                        res.append(1)
                        added = True
                    
                elif A[-i] != 9 and not added:
                    res.append(A[-i]+1)
                    added = True
                
                else:
                    res.append(A[-i])
                    
            return res[::-1]

if __name__=="__main__":
    arr = [9,9,9,9]
    print Solution().plusOne(arr)