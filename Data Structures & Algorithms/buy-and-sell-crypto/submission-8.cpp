class Solution {
public:
    int maxProfit(vector<int>& prices) {

        int left = 0;
        int right = 1;
        int max_profit = 0;
        int n = prices.size();

        while (right < n)
        {
            if (prices[right] < prices[left])
            {
                left = right;
            } 
            else if (prices[right] > prices[left])
            {
                int curr_profit = prices[right] - prices[left];
                max_profit = max(curr_profit,max_profit);
            }
            right++;
        }

        return max_profit;
        
    }
};
