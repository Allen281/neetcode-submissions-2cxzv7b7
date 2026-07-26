class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.empty()) return "";

        // Iterate through the characters of the first string
        for (int i = 0; i < strs[0].size(); i++) {
            char c = strs[0][i]; // Cache the character to check
            
            for (int j = 1; j < strs.size(); j++) {
                // If we reach the end of a string, or find a mismatch, return the substring
                if (i == strs[j].size() || strs[j][i] != c) {
                    return strs[0].substr(0, i); 
                }
            }
        }

        // If we make it through the whole loop, the entire first string is the prefix
        return strs[0];
    }
};