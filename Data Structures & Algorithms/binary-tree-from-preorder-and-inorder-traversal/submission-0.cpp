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
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if(preorder.empty()) return nullptr;

        TreeNode* root = new TreeNode(preorder[0]);

        vector<int> leftP, rightP, leftI, rightI;
        int i = 0;
        while(i+1 < inorder.size() && inorder[i] != root->val){
            leftI.push_back(inorder[i]);
            leftP.push_back(preorder[i+1]);
            i++;
        }
        i++;
        
        while(i < inorder.size()){
            rightI.push_back(inorder[i]);
            rightP.push_back(preorder[i]);
            i++;
        }

        root->left = buildTree(leftP, leftI);
        root->right = buildTree(rightP, rightI);

        return root;   
    }
};
