class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        NUM_Shards = 3
        shard = [{} for _ in range(NUM_Shards)]
        # shard = [ {} {} {} ]

        for string in strs:
            count = [0] * 26
            for char in string:
                index  = ord(char) - ord('a')
                count[index] += 1
            key = tuple(count)

            shard_id = hash(key) % NUM_Shards
            group = shard[shard_id]
            if key in group:
                group[key] += [string]
            else:
                group[key] = [string]

        result = []

        for shard in shard:
            result.extend(shard.values())

        return result


                

        