/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    bool exists(TreeNode* root , TreeNode* elem){
        if(root==nullptr || elem==nullptr) return false;
        if(root->val==elem->val) return true;
        if(root->left != nullptr && root->right != nullptr) return exists(root->left,elem) || exists(root->right,elem);
        if(root->left != nullptr ) return exists(root->left,elem) ;
        if(root->right != nullptr) return exists(root->right,elem);
        return false;
    }
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root==nullptr || p==nullptr || q==nullptr) return nullptr;
        TreeNode* i = root;
        while(i!=nullptr){
            if( (exists(i->left,p) && exists(i->right,q))
                || (exists(i->right,p) && exists(i->left,q))
                || (p==i && exists(i,q)) || (q==i && exists(i,p)) ) return i;
            if( (exists(i->left,p) && exists(i->left,q))) i=i->left;
            if( (exists(i->right,p) && exists(i->right,q))) i=i->right;
        }
        return i;
    }
};