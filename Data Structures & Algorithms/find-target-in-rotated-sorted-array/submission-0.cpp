class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0, right = nums.size();
        while(right-1 > left){
            int mid = (left+right)/2;

            if(nums[mid] < nums[0]) right = mid;
            else left = mid;
        }

        left++;

        if(target < nums[0] && left < nums.size()){
            right = nums.size();
        } else{
            right = left;
            left = 0;
        }

        while(right-1 > left){
            int mid = (left+right)/2;

            if(nums[mid] > target) right = mid;
            else left = mid;
        }

        return nums[left] == target ? left : -1;
    }
};