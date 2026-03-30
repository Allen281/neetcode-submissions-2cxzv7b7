class Solution {
public:
    int characterReplacement(string s, int k) {
        vector<int> counts(26);

        counts[s[0]-'A']++;
        int l = 0, r = 1, rslt = k, curMax = 1;
        while(r < s.size()){
            counts[s[r]-'A']++;

            curMax = max(curMax, counts[s[r]-'A']);

            if(r-l+1-curMax <= k){
                rslt = max(rslt, r-l+1);
            } else{
                while(r-l+1-curMax > k){
                    counts[s[l]-'A']--;
                    l++;
                }
            }

            r++;
        }

        return rslt;
    }
};
