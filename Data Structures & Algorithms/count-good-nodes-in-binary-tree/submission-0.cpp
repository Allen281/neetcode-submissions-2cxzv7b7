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
    int counter;
    int goodNodes(TreeNode* root) {
        counter = 0;
        solve(root, -101);

        return counter;
    }

    void solve(TreeNode* cur, int curMax){
        if(!cur) return;

        if(cur->val >= curMax) counter++;
        curMax = max(curMax, cur->val);

        solve(cur->left, curMax);
        solve(cur->right, curMax);
    }
};
