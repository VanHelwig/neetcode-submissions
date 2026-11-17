
class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []

        for s in strs:
            encoded.append(f"{len(s)}#{s}")

        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1

            word_len = int(s[i:j])
            i = j + 1
            decoded.append(s[i:i + word_len])
            i += word_len

        return decoded
