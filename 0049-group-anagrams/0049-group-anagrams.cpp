class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> h;
        for(int i = 0; i < strs.size(); i++){
            string temp = strs[i];
            sort(temp.begin(), temp.end());
            h[temp].push_back(strs[i]);
        }
        vector<vector<string>> ans;
        for(auto m: h) ans.push_back(m.second);
        return ans;
    }

    /*bool isAnagram(string s, string t) {
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

    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> res ;
        if(strs.size()==0) return res;
        if(strs.size()==1){res.push_back(strs); return res;}

        //for(vector<string>::iterator it=strs.begin() ; it!=strs.end() ; ++it){

        unordered_set<int> done_indices ;
        vector<string> a;
        for(int i=0;i<strs.size();i++){
            if(done_indices.find(i)!=done_indices.end()) continue;
            a.clear();
            a.push_back(strs.at(i));
            for(int j=i+1;j<strs.size();j++){
                if(done_indices.find(j)!=done_indices.end()) continue;
                if(isAnagram(strs.at(i) , strs.at(j)) ){
                    done_indices.insert(j);
                    a.push_back(strs.at(j));
                }
            }
            res.push_back(a);
        }
        return res;
    }*/


};