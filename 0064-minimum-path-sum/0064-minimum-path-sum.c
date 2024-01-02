int min(int a,int b){
    if(a<b) return a;
    return b;
}
int minPathSum(int** grid, int gridSize, int* gridColSize){
    int m=gridSize,n=*gridColSize;
    int tab[m][n];
    

    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            if(i==0 && j>0) tab[i][j]=grid[i][j]+tab[i][j-1];
            else if(j==0 && i>0) tab[i][j]=grid[i][j]+tab[i-1][j];
            else if(j==0 && i==0) tab[0][0]=grid[0][0];
            else tab[i][j]=grid[i][j]+min(tab[i][j-1],tab[i-1][j]);
        }
    }
    return tab[m-1][n-1];
}