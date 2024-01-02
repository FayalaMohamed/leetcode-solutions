class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size()!=t.size()) return false;
        int h[26]={0};                  //SC:O(26)~O(1)
        for(int i=0 ; i<s.size() ; i++){       //O(n)
            h[s[i]-'a']++;
            h[t[i]-'a']--;
        }
        for(int i=0 ; i<26 ; i++){      //O(26)~O(n)
            if(h[i])
                return false;
        }
        return true;
    }
};