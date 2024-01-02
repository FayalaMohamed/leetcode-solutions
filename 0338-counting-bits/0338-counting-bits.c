/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countBits(int n, int* returnSize){
    int* tab=malloc((n+1)*sizeof(int));
    *returnSize=n+1;
    
    tab[0]=0;
    for(int i=1;i<n+1;i++)
        tab[i]=tab[i>>1]+i%2;
    return tab;
}

