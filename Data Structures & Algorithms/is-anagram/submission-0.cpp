class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int> count(26);

        if(s.size() != t.size()) return false;

        for(int i = 0; i < s.size(); i++){
            count[s[i]-'a']++;
            count[t[i]-'a']--;
        }

        for(int c : count) if(c != 0) return false;

        return true;
    }
};
