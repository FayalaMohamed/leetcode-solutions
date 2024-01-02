int val(int ligne,int colonne,int m,int n,int tab[m][n] ){
    if(ligne==0 || colonne == 0){
        tab[ligne][colonne]=1;
        return 1;
    }
    if(tab[ligne-1][colonne]==0)
        tab[ligne-1][colonne]=val(ligne-1 ,colonne,m,n,tab);
    if(tab[ligne][colonne-1]==0)
        tab[ligne][colonne-1]=val(ligne ,colonne-1,m,n,tab);
    tab[ligne][colonne]=tab[ligne-1][colonne]+tab[ligne][colonne-1];
    return tab[ligne][colonne];
}

int uniquePaths(int m, int n){
    int tab[m][n];
    for(int i=0 ;i<m;i++){
        for(int j = 0 ; j<n ;j++ ){
            tab[i][j]=0;
        }
    }
    if(m==1 && n==1) return 1;
    return val(m-1,n-1,m,n,tab);
}