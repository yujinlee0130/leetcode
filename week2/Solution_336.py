class Solution_336:

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def isPalindrome(word):
            return word == word[::-1]
        
        # save every word in hashmap
        # for each word, reverse [::-1] and check if exists in hash. 
        wordmap = {word: i for i, word in enumerate(words)}
        ans = []

        for idx, word in enumerate(words):
            # if word = " " and the other word is a palindrome, add that pair
            if word == ' ':
                for j, w in enumerate(words):
                    if idx != j and isPalindrome(w):
                        ans.append([idx,w], [w,idx])

            # iterating through each split
            for i in range(0, len(word)+1):
                # 1. reverse-prefix exists as another word 
                # 2. the reverse-prefix shouldn't be itself
                # 3. the suffix should be a palindrome
                prefix, suffix = word[:i], word[i:]

                if prefix[::-1] in wordmap and wordmap[prefix[::-1]] != idx and isPalindrome(suffix):
                    ans.append([wordmap[word], wordmap[prefix[::-1]]])

                # reverse-suffix exists as another word
                if len(suffix[::-1]) != len(word) and suffix[::-1] in wordmap and wordmap[suffix[::-1]] != idx and isPalindrome(prefix):
                    ans.append([wordmap[suffix[::-1]], wordmap[word]])
                

        return ans
                
            