class Solution {
public:
    int trap(vector<int>& height) {
        if(height.size() < 2) return 0;
        int left = 0, right = 1;

        int rslt = 0, blocks = 0;
        while(right < height.size()){
            if(height[right] >= height[left]){
                rslt += (right-left-1)*height[left] - blocks;
                blocks = 0;
                left = right;
            } else{
                blocks += height[right];
            }

            right++;
        }

        right--;
        blocks = 0;
        int tempLeft = right-1;

        while(tempLeft >= left){
            if(height[tempLeft] >= height[right]){
                rslt += (right-tempLeft-1)*height[right] - blocks;
                blocks = 0;
                right = tempLeft;
            } else{
                blocks += height[tempLeft];
            }

            tempLeft--;
        }

        return rslt;
    }
};