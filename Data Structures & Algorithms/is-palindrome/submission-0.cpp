class Solution {
public:
    bool isPalindrome(string s) {
        transform(s.begin(), s.end(), s.begin(), [](unsigned char c){ return tolower(c);});
        int lp = 0, rp = s.size()-1;
        while(lp < rp){
            char left = s[lp], right = s[rp];

            if(outBounds(left)){
                lp++;
            } else if(outBounds(right)){
                rp--;
            } else if(right != left){
                return false;
            } else{
                lp++;
                rp--;
            }
        }

        return true;
    }

    bool outBounds(char c){
        return (c < 'a' || c > 'z') && (c < '0' || c > '9');
    }
};
