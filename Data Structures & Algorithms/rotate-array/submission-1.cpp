class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k = k % n;
        if (k == 0) return;

        int elementsPlaced = 0; 

        for (int i = 0; elementsPlaced < n; i++) {
            
            int curIndex = (i + k) % n;
            int lastVal = nums[i];
            
            while (curIndex != i) {
                swap(nums[curIndex], lastVal);
                curIndex = (curIndex + k) % n;
                elementsPlaced++;
            }

            swap(nums[curIndex], lastVal);
            elementsPlaced++; 
        }
    }
};