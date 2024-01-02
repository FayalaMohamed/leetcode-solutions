bool isSubsequence(char * s, char * t){
    int jFound=0;
    for(int i=0;i<strlen(t);i++){
        if(t[i]==s[jFound]) jFound++;
    }

    if(jFound==strlen(s)) return true;
    return false;
}