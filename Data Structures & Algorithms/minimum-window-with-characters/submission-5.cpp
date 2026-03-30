class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> leftOver;
        unordered_set<char> needed;
        unordered_set<char> chars;

        for(char c : t){
            leftOver[c]++;
            chars.insert(c);
            needed.insert(c);
        }

        int l = 0, r = 0;
        string rslt = "";

        while(r < s.size()){
            char cur = s[r];

            if(chars.count(cur)){
                leftOver[cur]--;
                if(leftOver[cur] <= 0) needed.erase(cur);
                else needed.insert(cur);
            }

            while(needed.empty()){
                if(r-l+1 < rslt.size() || rslt == "") rslt = s.substr(l, r-l+1);

                leftOver[s[l]]++;
                if(leftOver[s[l]] > 0 && chars.count(s[l])) needed.insert(s[l]);
                l++;
            }

            r++;
        }

        return rslt;   
    }
};
