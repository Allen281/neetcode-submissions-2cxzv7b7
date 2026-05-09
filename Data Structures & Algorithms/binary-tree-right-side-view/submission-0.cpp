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
    unordered_set<int> levels;
    vector<int> rslt;
    vector<int> rightSideView(TreeNode* root) {
        traverse(root, 0);
        return rslt;
    }

    void traverse(TreeNode* cur, int level){
        if(!cur) return;

        if(!levels.contains(level)){
            rslt.push_back(cur->val);
            levels.insert(level);
        }

        traverse(cur->right, level+1);
        traverse(cur->left, level+1);
    }
};
