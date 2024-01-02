int tribonacci(int n){
    int tab[n+3];
    tab[0]=0;
    tab[1]=1;
    tab[2]=1;
    for(int i=3;i<=n;i++) tab[i]=tab[i-1]+tab[i-2]+tab[i-3];
    return tab[n];
}