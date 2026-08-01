class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        std::unordered_map<int,int> seen;

        for (size_t idx = 0; idx < nums.size(); ++idx)
        {
            int num = nums[idx];
            int diff = target - num;

            if (seen.find(diff) != seen.end())
            {
                return {seen[diff], (int)idx};
            }
            else
            {
                seen[num] = (int)idx;
            }
        }

        return {};
        
    }
};
