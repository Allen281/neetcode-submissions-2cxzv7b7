class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;

        vector<int> runningMax(prices.size());
        runningMax[prices.size()-1] = prices[prices.size()-1];

        for(int i = prices.size()-2; i >= 0; i--){
            runningMax[i] = max(runningMax[i+1], prices[i]);
        }

        for(int i = 0; i < prices.size(); i++){
            profit = max(profit, runningMax[i]-prices[i]);
        }

        return profit;
    }
};
