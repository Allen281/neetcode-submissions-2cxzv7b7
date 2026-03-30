class Solution {
public:
    int maxArea(vector<int>& heights) {
        int rslt = 0;
        int l = 0, r = heights.size()-1;
        while(l < r){
            if(heights[l] < heights[r]){
                rslt = max(rslt, heights[l]*(r-l));
                l++;
            } else{
                rslt = max(rslt, heights[r]*(r-l));
                r--;
            }
        }
        return rslt;
    }

};
