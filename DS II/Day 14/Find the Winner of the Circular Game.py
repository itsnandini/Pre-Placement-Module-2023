class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [False] * n
        friendCount = n
        fp = 0
        while friendCount > 1:
            for _ in range(k):
                while friends[fp % n]: 
                    fp += 1  
                fp +=1
            friends[(fp - 1) % n] = True
            friendCount -= 1

        fp = 0
        while friends[fp]:
            fp += 1

        return fp + 1
