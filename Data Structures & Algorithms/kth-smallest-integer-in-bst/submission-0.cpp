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
    void levelOrder(TreeNode* root, int k){
        if(counter >= k) return;
        if(root == nullptr) return;

        levelOrder(root->left, k);
        if(counter < k){
            rslt = root->val;
            counter++;
        }
        levelOrder(root->right, k);
    }

    int counter = 0;
    int rslt = 0;
    int kthSmallest(TreeNode* root, int k) {
        levelOrder(root, k);

        return rslt;
    }

};
