class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int left = 0, right = arr.size()-1;
        while(left+1 < right){
            int mid = (left+right)/2;
            if(arr[mid] <= x) left = mid;
            else right = mid;
        }

        if(k == 1) return arr[right]-x < x-arr[left] ? vector<int>{arr[right]} : vector<int>{arr[left]};

        while(right-left < k){
            if(left <= 0 && right >= arr.size()) break;
            else if(left <= 0){
                right++;
            } else if(right >= arr.size()){
                left--;
            } else{
                if(arr[right]-x < x-arr[left-1]) right++;
                else left--;
            }
        }

        return vector<int>(arr.begin()+left, arr.begin()+right);
    }
};