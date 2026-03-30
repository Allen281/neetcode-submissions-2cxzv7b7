class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> leftProduct(nums.size()+2);
        vector<int> rightProduct(nums.size()+2);
        leftProduct[0] = rightProduct[0] = 1;
        leftProduct[nums.size()+1] = rightProduct[nums.size()+1] = 1;

        for(int i = 1, j = nums.size(); i <= nums.size(); i++, j--){
            leftProduct[i] = nums[i-1]*leftProduct[i-1];
            rightProduct[j] = nums[j-1]*rightProduct[j+1];
        }

        vector<int> rslt(nums.size());
        for(int i = 1; i <= nums.size(); i++){
            rslt[i-1] = leftProduct[i-1]*rightProduct[i+1];
        }

        return rslt;
    }
};
