int getMaximumGenerated(int n){
    if(n==0) return 0;
    int max=0;
    int tab[n+1];
    tab[0]=0;
    tab[1]=1;
    for(int i=0;i<=n;i++){
        if(i%2==0){
            tab[i]=tab[i/2];
        }
        if(i%2==1){ 
            tab[i]=tab[i/2]+tab[i/2+1];
        }
        if(tab[i]>max) max=tab[i];
    }
    return max;
}