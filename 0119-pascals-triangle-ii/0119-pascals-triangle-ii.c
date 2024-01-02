/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getRow(int rowIndex, int* returnSize){
    int** tab =malloc(sizeof(int*)*(rowIndex+1));
    for(int i=0;i<=rowIndex;i++){
        *(tab+i)=malloc(sizeof(int)*(i+1));
        *(*(tab+i))=*(*(tab+i)+i)=1;
        for(int j=1;j<i;j++) *(*(tab+i)+j)=*(*(tab+i-1)+j) + *(*(tab+i-1)+j-1);
    }
    *returnSize=rowIndex+1;
    return *(tab+rowIndex);

}

