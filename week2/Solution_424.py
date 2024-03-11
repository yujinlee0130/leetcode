class Solution_424:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        start, end = 0, 0
        maxfreq, maxlen = 0,0
        
        while (end < len(s)):
            freq[s[end]] += 1
            maxfreq = max(maxfreq, freq[s[end]])
            # compare the window size - max frequency of that window
            # if that is < k, keep going
            # otherwise, increment start
            if (end-start+1)-maxfreq > k:
                freq[s[start]] -= 1
                start += 1
            maxlen = max(maxlen, end-start + 1)
            end += 1

        return maxlen

            
            