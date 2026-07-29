class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {

        // piles = [1,4,3,2], h = 9

        // minimum rate to eat up all banana
        // while cost time < h

        int rate_left = 1;
        int rate_right = *max_element(piles.begin(),piles.end());

        int rate_ans = rate_right;

        while (rate_left<=rate_right)
        {
            int rate_mid = rate_left + (rate_right - rate_left) / 2;

            // piles.length <= h <= 10^9
            // 1 <= piles[i] <= 10^9
            // to prevent overflow
            long long total_cost_hr = 0;

            for (int banana: piles)
            {
                // Calculate ceil : (X + (mid - 1) ) / mid 
                total_cost_hr += (banana + rate_mid - 1) / rate_mid;
            }

            // rate now is too slow
            if (total_cost_hr > h) rate_left = rate_mid + 1;
            // rate now is equal to h or even lesser
            else
            {
                // keep the ans first
                rate_ans = rate_mid;
                // check if smaller rate so far possible
                rate_right = rate_mid - 1;
            }

        }

        return rate_ans;
    }
};
