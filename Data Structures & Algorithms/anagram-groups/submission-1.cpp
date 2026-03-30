class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, vector<string>> groups;

        for(string s : strs){
            vector<int> counts(26);
            for(char c : s){
                counts[c-'a']++;
            }

            string key = "";
            for(int c : counts) key += to_string(c) + ",";

            groups[key].push_back(s);
        }

        vector<vector<string>> rslt;
        for(const auto& group : groups){
            rslt.push_back(group.second);
        }

        return rslt;
    }
};
