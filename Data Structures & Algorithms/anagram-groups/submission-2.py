class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}

        for word in strs:
            count = [0] * 26

            for char in word:
                alpha_position = ord(char) - ord('a')
                count[alpha_position] += 1

            signature = tuple(count)

            if signature in groups:
                groups[signature].append(word)

            else:
                groups[signature] = [word]
            
        return list(groups.values())
        
