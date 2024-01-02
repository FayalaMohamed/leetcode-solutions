class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> dict(256, -1);
        int maxLen = 0, start = -1;
        for (int i = 0; i != s.length(); i++) {
            if (dict[s[i]] > start)
                start = dict[s[i]];
            dict[s[i]] = i;
            maxLen = max(maxLen, i - start);
        }
        return maxLen;
        /* marhce pas : les sets ne sont pas ordonnés par ordre d'insertion
           meme unordered_set : hashage
        unordered_set<char> mySet ;
        int maxi=0 ;
        for(char c : s){
            while(mySet.count(c)==1) mySet.erase(mySet.begin());
            if(!mySet.insert(c).second){
                
            }
            if(mySet.size()>maxi) maxi=mySet.size();
        }
        return maxi;*/
    }
};