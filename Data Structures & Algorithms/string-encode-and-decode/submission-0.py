class Solution:

    def encode(self, strs: List[str]) -> str:

        # dummy_input = ["Hello","World"]
        # "Hello" -> n = len(Hello) = 5
        # 5 + # + string 

        result = []

        for string in strs:
            n = len(string)
            encoded_part = f"{n}#{string}"
            result.append(encoded_part)

            # result ["5#Hello5#World"]

        return "".join(result)

    def decode(self, s: str) -> List[str]:

        result = []
        i = 0

        while i < len(s):

            j = s.find("#",i)

            length = int(s[i:j])

            target_word = s[j+1:j+1+length]
            result.append(target_word)

            i  = j+1+length

        return result












