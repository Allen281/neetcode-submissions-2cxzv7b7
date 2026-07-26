class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        return mergeSort(nums, 0, nums.size());
    }

private:
    vector<int> mergeSort(vector<int>& nums, int start, int end){
        if(start+1 == end) return {nums[start]};

        int mid = (start+end)/2;
        vector<int> first = mergeSort(nums, start, mid);
        vector<int> second = mergeSort(nums, mid, end);

        vector<int> rslt;
        int p1 = 0, p2 = 0;

        while(true){
            if(p1 >= first.size() && p2 >= second.size()) return rslt;
            else if(p1 >= first.size()){
                rslt.push_back(second[p2++]);
            } else if(p2 >= second.size()){
                rslt.push_back(first[p1++]);
            } else{
                rslt.push_back(first[p1] < second[p2] ? first[p1++] : second[p2++]);
            }
        }
    }
};