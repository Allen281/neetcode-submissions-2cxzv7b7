class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        vector<int> temp(nums);
        mergeSort(nums, temp, 0, nums.size());
        return nums;
    }

private:
    void mergeSort(vector<int>& nums, vector<int>& temp, int start, int end){
        if(start+1 == end){
            temp[start] = nums[start];
            return;
        }

        int mid = (start+end)/2;
        mergeSort(temp, nums, start, mid);
        mergeSort(temp, nums, mid, end);

        int p1 = start, p2 = mid, i = start;

        while(p1 < mid && p2 < end){
            nums[i++] = temp[p1] < temp[p2] ? temp[p1++] : temp[p2++];
        }

        while(p1 < mid) nums[i++] = temp[p1++];
        while(p2 < end) nums[i++] = temp[p2++];
    }
};