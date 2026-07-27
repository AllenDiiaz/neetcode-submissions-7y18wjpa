class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {

        int left = 1;
        int right = *max_element(piles.begin(),piles.end());

        int ans = right;

        while (left<=right)
        {
            int mid = left + (right-left) / 2;
            long long total_cost = 0;

            for (int p: piles) 
            {
                total_cost += ( p + mid - 1) / mid; // ceil( p / mid)
            }

            if (total_cost > h)
            {
                left = mid + 1;
            }
            else
            {
                ans = mid;
                right = mid - 1;
            }
        }

        return ans;     
    }
};
