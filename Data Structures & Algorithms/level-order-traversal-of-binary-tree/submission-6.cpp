/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        if(root == nullptr) return {};

        queue<TreeNode*> q;
        q.push(root);

        vector<vector<int>> rslt;
        int counter = 1;
        while(true){
            TreeNode* cur = q.front();
            q.pop();

            int level = log2(counter++);
            if(rslt.size() <= level) rslt.push_back({});

            if(cur == nullptr){
                q.push(nullptr);
                q.push(nullptr);
            }else{
                rslt[level].push_back(cur->val);
                q.push(cur->left);
                q.push(cur->right);
            }
            
            if(level > 0 && rslt[level-1].empty()) break;
        }

        for(int i = 0; i < rslt.size(); i++){
            if(rslt[i].empty()){
                rslt.erase(rslt.begin()+i);
                i--;
            }
        }
        return rslt;
    }
};
