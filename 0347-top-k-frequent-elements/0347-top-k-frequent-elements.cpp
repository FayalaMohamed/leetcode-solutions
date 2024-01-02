class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int,int> nb;
        map<int,vector<int>> maMap;
        vector<int> res;
        
        //nb sous la forme : {entier , nbOccurences}
        for(auto i : nums){
            if(nb.count(i)==0) nb.insert(pair(i,1));
            else ++nb[i];
        }

        //maMap sous forme {nbOccurences , {liste des éléments avec un tel nb d'occurence} }
        for(int i=0; i<=nums.size();i++){
            pair<int,vector<int>> paire;
            paire.first=i;
            vector<int> v;
            paire.second = v;
            maMap.insert(paire);
        }
        for( map<int,int>::iterator it= nb.begin() ; it!=nb.end() ;it++ ){
            maMap[(*it).second].push_back((*it).first);
        }
        

        int done=0;
        for( map<int,vector<int>>::reverse_iterator it= maMap.rbegin() ; it!=maMap.rend() ;it++ ){
            //if((*it).second.size()==0) continue;
            while(!(*it).second.empty() && done!=k){
                res.push_back((*it).second.back());
                //(*it).second.erase(--(*it).second.end());
                (*it).second.pop_back();
                done++;
            }

            if(done==k) break;
            
        }


        return res;
    }
};