class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int p1 = 0, p2 = 0;
        bool isFirst = true;
        string rslt = "";

        while(p1 < word1.size() && p2 < word2.size()){
            rslt += isFirst ? word1[p1++] : word2[p2++];
            isFirst = !isFirst;
        }

        while(p1 < word1.size()) rslt += word1[p1++];
        while(p2 < word2.size()) rslt += word2[p2++];

        return rslt;
    }
};