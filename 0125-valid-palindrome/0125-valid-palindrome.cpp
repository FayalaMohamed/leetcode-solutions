class Solution {
public:
    bool isPalindrome(string s) {
        int end=s.size()-1 , i=0;
        while(i<end){
            if(!iswalnum(s[i])) {i++; continue;}
            if(!iswalnum(s[end])) {end--; continue;}
            if(tolower(s[i]) != tolower(s[end])) return false ;
            i++; end--;
        }
        return true;
    }
};