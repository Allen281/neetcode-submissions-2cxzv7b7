class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int lastElement = nums.size()-1;
        for (int i = 0; i <= lastElement; i++){
            if (nums[i] == val) {
                nums[i--] = nums[lastElement--];
            }
        }

        return lastElement+1;
    }
};