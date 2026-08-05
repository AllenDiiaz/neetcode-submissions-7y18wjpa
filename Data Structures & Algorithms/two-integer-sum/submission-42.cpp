class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        // nums = [3,4,5,6], target = 7
        // seen [3:0,4:1,....]

        std::unordered_map<int,int> seen;

        int n = nums.size();

        for (int i=0; i < n ; ++i)
        {
            int num = nums[i];
            int diff = target - num;

            if (seen.find(diff) == seen.end())
            {
                seen[num] = i;
            } else {
                return {seen[diff],i};
            }
        }
        
        return {};
    }
};
