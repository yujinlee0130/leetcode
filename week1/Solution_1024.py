class Solution_1024:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        # recursion
        # dp(i) = min number of clips needed 
        # dp(i) = min(dp(i),  dp(start) + 1)
        DP = [float(inf)] * (time + 1)
        DP[0] = 0

        for i in range(1, time+1):
            for start, end in clips:
                # Iteratively update the DP array 
                # for each time point by considering all clips 
                # that can contribute to reaching that time point
                if start <= i <= end:
                    DP[i] = min(DP[i], DP[start] + 1)
        
        if DP[time] != float(inf):
            return DP[time]
        else:
            return -1 