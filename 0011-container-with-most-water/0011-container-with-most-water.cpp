class Solution {
public:
    int maxArea(vector<int>& height) {
        int i=0 , end = height.size()-1 , max=0; 
        while(i<end){
            if(min(height[i],height[end])*(end-i)>max) max= min(height[i],height[end])*(end-i) ;
            if(height[i]<height[end]) i++;
            else if(height[i]>=height[end]) end--;
        }
        return max;
    }
};