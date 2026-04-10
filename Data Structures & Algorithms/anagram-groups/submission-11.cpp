class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {

        std::map<vector<int>, vector<string>> group;

        for (string const& str: strs) {

            std::vector<int> count(26,0);

            for (char const& c: str) {

                count[c-'a']++;
            }
            group[count].push_back(str);
        }

        vector<vector<string>> result;

        for (auto const& [key, val]: group) {

            result.push_back(val);
        }

        return result;
        
    }
};
