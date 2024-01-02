bool canJump(int* nums, int numsSize){
    bool tab[numsSize];
    tab[0]=true;
    for(int i=1;i<numsSize;i++){
        tab[i]=false;
        for(int j=i-1;j>=0;j--){
            tab[i]=(tab[j] && nums[j]>=i-j )&& nums[j]>0;
            if(tab[i]) break;
        }
    }
    return tab[numsSize-1];
}