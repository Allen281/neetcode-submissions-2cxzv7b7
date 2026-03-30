class Solution {
public:
    int climbStairs(int n) {
        if(n == 1) return 1;
        if(n == 2) return 2;

        int oneDown = 1, twoDown = 1;
        int rslt = 0;
        n -= 1;
        while(n--){
            rslt = oneDown + twoDown;
            twoDown = oneDown;
            oneDown = rslt;
        }

        return rslt;
    }
};
