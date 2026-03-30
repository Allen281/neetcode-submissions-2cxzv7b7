class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> used;

        int l = 0, r = 0, rslt = 0;
        while(r < s.size()){
            if(used[s[r]]){
                while(l < s.size() && s[l] != s[r]) used[s[l++]] = false;
                l++;
                used[s[r]] = false;
            } else{
                used[s[r]] = true;
                rslt = max(rslt, r-l+1);
                r++;
            }
        }

        return rslt;
    }
};
