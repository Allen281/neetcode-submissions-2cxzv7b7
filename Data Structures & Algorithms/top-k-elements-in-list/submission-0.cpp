class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> counts;

        for(int n : nums) counts[n]++;

        vector<pair<int, int>> mostFreq;

        for(const auto& pair : counts){
            mostFreq.push_back({1e4-pair.second, pair.first});
        }

        sort(mostFreq.begin(), mostFreq.end());

        vector<int> rslt;
        for(int i = 0; i < k; i++){
            rslt.push_back(mostFreq[i].second);
        }

        return rslt;
    }
};
