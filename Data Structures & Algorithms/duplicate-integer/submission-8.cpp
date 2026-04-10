class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {

        std::unordered_set<int> seen;

        for (size_t i = 0; i < nums.size(); ++i) {

            int num = nums[i];
            if (seen.find(num) != seen.end()) {

                return true;
            }
            seen.insert(num);
        }
        return false;   
    }
};