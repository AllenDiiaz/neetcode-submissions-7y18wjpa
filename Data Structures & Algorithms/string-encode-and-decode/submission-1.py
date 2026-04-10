class Solution:

    def encode(self, strs: List[str]) -> str:

        # strs = ["Hello","World"]
        # return -> "5#Hello5#World"

        result = []

        for string in strs:
            length = len(string)
            encode = f"{length}#{string}"
            result.append(encode)

        return "".join(result)

    def decode(self, s: str) -> List[str]:

        # s = "5#Hello5#World"

        res = []
        i = 0

        while i < len(s):

            j = s.find("#",i)
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            res.append(word)

            i = j + 1 + length

        return res










