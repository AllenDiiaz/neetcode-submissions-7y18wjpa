class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        std::unordered_map<int, int> seen;

        int n = nums.size();

        for (size_t i = 0; i < n; ++i) {

            int num = nums[i];
            int diff = target - num;

            if (seen.find(diff) != seen.end()) {

                return {seen[diff],static_cast<int>(i)};
            }

            seen[num] = i;
        }

        return {};
        
    }
};
