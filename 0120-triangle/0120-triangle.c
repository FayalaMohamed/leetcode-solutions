int min(int a,int b){
    if(a<b) return a;
    return b;
}

int minimumTotal(int** triangle, int triangleSize, int* triangleColSize){
    for(int i=1;i<triangleSize;i++){
        for(int j=0;j<*(triangleColSize+i);j++){
            if(j==0) triangle[i][j] += triangle[i-1][j];
            else if(j==*(triangleColSize+i)-1) triangle[i][j] += triangle[i-1][j-1];
            else triangle[i][j] += min(triangle[i-1][j-1],triangle[i-1][j]);
        }
    }
    int minTab=triangle[triangleSize-1][0];
    for(int j=1;j<*(triangleColSize+triangleSize-1);j++){
        if(triangle[triangleSize-1][j]<minTab) minTab=triangle[triangleSize-1][j];
    }
    return minTab;
}

