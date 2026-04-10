class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        std::unordered_map<int, int> seen;

        for (size_t i = 0; i < nums.size(); ++i) {

            int num  = nums[i];
            int diff = target - num;

            if (seen.find(diff) != seen.end()) {

                return {seen[diff], static_cast<int>(i)};
            }

            seen[num] = static_cast<int>(i);
        }

        return {}; 
    }
};
