class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        DELIMITER = '#'

        for s in strs:
            prefix = str(len(s)) + DELIMITER
            encoded = ''.join([encoded, prefix])

            for char in s:
                encoded = ''.join([encoded, char])
        
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        DELIMITER = '#'
        word = ''
        word_len = 0
        len_str = ''
        i = 0

        while i < len(s):
            getting_prefix = True

            while getting_prefix:
                if s[i] != DELIMITER:
                    len_str = ''.join([len_str, s[i]])
                    i += 1
                
                else:
                    word_len = int(len_str)
                    i += 1
                    getting_prefix = False
            
            while not getting_prefix:
                for _ in range(word_len):
                    word = ''.join([word, s[i]])
                    i += 1
                
                decoded.append(word)
                word = ''
                word_len = 0
                len_str = ''
                getting_prefix = True
            
        return decoded

           
                




       

            