int removeElement(int* nums, int numsSize, int val){
    int nb=0,i=0;
    while(i<numsSize-nb){
        if(nums[i]==val){
            for(int j=i;j<numsSize-nb-1;j++) nums[j]=nums[j+1];
            nb++;
        }else{
            i++;
        }
    }
    return numsSize-nb;
}