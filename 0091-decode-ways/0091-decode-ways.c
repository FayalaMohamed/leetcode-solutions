int numDecodings(char * s){
    int n=0;
    while(*(s+n)!='\0') n++;
    if(n==0) return 0;
    if(*s=='0') return 0;

    int tab[n][2];
    tab[0][0]=1;
    tab[0][1]=0;

    for(int i=1;i<n;i++){
        tab[i][0]=tab[i-1][0]+tab[i-1][1];
        tab[i][1]=tab[i-1][0];
        if(*(s+i)=='0' ) tab[i][0]=0;
        if(*(s+i-1)=='0' || (*(s+i-1)=='2' && *(s+i)>='7') || *(s+i-1)>='3' ) tab[i][1]=0;
    }

    return tab[n-1][0]+tab[n-1][1];
}