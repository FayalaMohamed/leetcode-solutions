int max(int a,int b){
    if(a<b) return b;
    return a;
}

int jump(int* nums, int numsSize){
    int jumps = 0, curEnd = 0, curFarthest = 0;
	for (int i = 0; i < numsSize - 1; i++) {
		curFarthest = max(curFarthest, i + nums[i]);
		if (i == curEnd) {
			jumps++;
			curEnd = curFarthest;
		}
	}
	return jumps;
}