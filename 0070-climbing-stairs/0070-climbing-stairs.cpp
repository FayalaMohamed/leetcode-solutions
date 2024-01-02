class Solution {
public:
    int climbStairs(int n) {
        int n_2=1,n_1=2,res;
        if(n<=2) return n;
        for(int i=3;i<=n;i++){
            res=n_2+n_1;
            n_2=n_1;
            n_1=res;
        }
        return res;
    }
};