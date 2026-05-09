class Solution {
public:
    static bool cmp(vector<int>& a, vector<int>& b){
        int aDist = pow(a[0], 2) + pow(a[1], 2);
        int bDist = pow(b[0], 2) + pow(b[1], 2);

        return aDist < bDist;
    }

    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        sort(points.begin(), points.end(), cmp);

        vector<vector<int>> rslt(points.begin(), points.begin()+k);

        return rslt;
    }
};
