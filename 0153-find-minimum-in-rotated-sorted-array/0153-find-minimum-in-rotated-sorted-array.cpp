class Solution {
public:
    int findMin(vector<int>& nums) {
        int min = nums[0];
        int left = 0 , right = nums.size()-1;
        while (nums[left]!=nums[right]){
            if(nums[left]>nums[right]) left++;
            else if(nums[left]<nums[right]) right--;
        }
        return nums[left];
        
    }
};