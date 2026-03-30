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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if(p == nullptr || q == nullptr){
            return p == q;
        }

        bool good = p->val == q->val;
        good = good && isSameTree(p->left, q->left);
        good = good && isSameTree(p->right, q->right);

        return good;
    }

    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if(root == nullptr){
            return isSameTree(root, subRoot);
        }

        if(root->val == subRoot->val){
            if(isSameTree(root, subRoot)) return true;
        }

        if(isSubtree(root->left, subRoot)) return true;
        if(isSubtree(root->right, subRoot)) return true;

        return false;
    }
};
