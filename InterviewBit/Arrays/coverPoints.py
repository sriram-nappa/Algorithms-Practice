class Solution:
    # @param X : list of integers
    # @param Y : list of integers
    # Points are represented by (X[i], Y[i])
    # @return an integer
    def coverPoints(self, X, Y):
        total = 0
        curX = X[0]
        curY = Y[0]
        for i in range(1, len(X)):
            total += max(abs(curX - X[i]), abs(curY - Y[i]))
            curX = X[i]
            curY = Y[i]
        return total

if __name__ == "__main__":
    arr1 = [1, -3, -5, 9]
    arr2 = [2, 1, -3, -2]
    print Solution().coverPoints(arr1, arr2)