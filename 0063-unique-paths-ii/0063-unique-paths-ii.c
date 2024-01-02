int uniquePathsWithObstacles(int** obstacleGrid, int obstacleGridSize, int* obstacleGridColSize){
    int m=obstacleGridSize;
    int n= *obstacleGridColSize;
    int array[m][n];
    for(int i = 0;i < m;i++) //ligne
        for(int j = 0;j < n;j++){ //colonne
            if(obstacleGrid[i][j]==1){
                array[i][j]=0;
                continue;
            }
            if(i == 0  ){
                bool test= true;
                for(int k=0;k<j;k++)
                    if(array[i][k]==0) test=false;
                if(test) array[i][j]=1;
                else array[i][j]=0;
            }else if( j == 0  ){
                bool test= true;
                for(int k=0;k<i;k++)
                    if(array[k][j]==0) test=false;
                if(test) array[i][j]=1;
                else array[i][j]=0;
            }else
                array[i][j] = array[i-1][j] + array[i][j-1];
            
        }
    return array[m-1][n-1];
}