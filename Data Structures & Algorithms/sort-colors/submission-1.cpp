class Solution {
public:
    void sortColors(vector<int>& nums) {
        int redP = 0, blueP = nums.size()-1;

        for(int i = redP; i <= blueP; i++){
            while(redP <= blueP && nums[redP] == 0) redP++;
            while(blueP > redP && nums[blueP] == 2) blueP--;
            
            if(i < redP) continue;
            if(blueP <= redP) return;

            if(nums[i] == 0){
                nums[i] = nums[redP];
                nums[redP++] = 0;
                i--;
            }
            else if(nums[i] == 2){
                nums[i] = nums[blueP];
                nums[blueP--] = 2;
                i--;
            }
        }
    }
};