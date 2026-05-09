class Solution {
public:
    struct Compare {
        bool operator()(vector<int>& a, vector<int>& b){
            int aDist = pow(a[0], 2) + pow(a[1], 2);
            int bDist = pow(b[0], 2) + pow(b[1], 2);
            return aDist < bDist;
        }
    };

    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<vector<int>, vector<vector<int>>, Compare> pq;

        for(vector<int> v: points){
            pq.push(v);

            if(pq.size() > k) pq.pop();
        }

        vector<vector<int>> rslt;
        for(int i = 0; i < k; i++){
            rslt.push_back(pq.top());
            pq.pop();
        }

        return rslt;
    }
};
