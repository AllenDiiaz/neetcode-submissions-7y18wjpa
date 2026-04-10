class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        // nums = [3,4,5,6]
        
        for (size_t i = 0; i< nums.size(); ++i){
            for (size_t j = i + 1; j < nums.size(); ++j){

                int diff = target - nums[i];

                if (diff == nums[j]){
                    return {static_cast<int>(i),static_cast<int>(j)};
                    }
            }
        }
    }
};