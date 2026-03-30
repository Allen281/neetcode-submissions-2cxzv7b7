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
    bool isValidBST(TreeNode* root) {
        if(root == nullptr) return true;

        if(root->left != nullptr && findMaxNode(root->left) >= root->val) return false;
        if(root->right != nullptr && findMinNode(root->right) <= root->val) return false;

        if(!isValidBST(root->left)) return false;
        if(!isValidBST(root->right)) return false;

        return true;
    }

    int findMaxNode(TreeNode* root){
        if(root == nullptr) return INT_MIN;

        int leftMax = findMaxNode(root->left);
        int rightMax = findMaxNode(root->right);

        return max(root->val, max(leftMax, rightMax));
    }

    int findMinNode(TreeNode* root){
        if(root == nullptr) return INT_MAX;

        int leftMax = findMinNode(root->left);
        int rightMax = findMinNode(root->right);

        return min(root->val, min(leftMax, rightMax));
    }
};
