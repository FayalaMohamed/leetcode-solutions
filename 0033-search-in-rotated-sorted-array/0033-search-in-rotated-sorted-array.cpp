class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0 , r = nums.size()-1,m=0;
        int where=-1;
        while(l<=r){
            if(nums[l]==target) return l;
            if(nums[r]==target) return r;
            m=(l+r)/2;
            if(nums[m]==target) return m;
            
            if(nums[l]<=nums[m]){
                if( nums[m]<target || target<nums[l]) l=m+1 ;
                else r=m-1;
            }else {
                if( nums[m]>target || target>nums[l]) r=m-1 ;
                else l=m+1;
            }

        }
        return where;
    }
};