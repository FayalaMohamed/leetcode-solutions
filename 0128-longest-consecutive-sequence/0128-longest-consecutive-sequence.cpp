/*class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.empty()){ return 0; }
        if(nums.size()==0 || nums.size()==1) return nums.size();

        unordered_map<int,bool> myMap;
        for(int i :nums){
            myMap.insert(pair<int,bool>(i,false));
        }

        int nbMax=0, next, maxActuel=1;
        for(int i :nums){
            if(myMap[i]) continue;
            maxActuel=1;
            next=i+1;
            while(myMap.count(next)==1){
                myMap[next]=true;
                next++;
                maxActuel++;
            }
            if(maxActuel>nbMax) nbMax=maxActuel;
        }

        return nbMax;
    }
};*/

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.empty()){return 0;}
        set<int>s;
        int ans=1;
        for(int i=0; i<nums.size(); i++){
            s.insert(nums[i]);
        }
        for(auto it=s.begin(); it!=s.end(); it++){
            int num=*it;
            if(s.find(num-1)==s.end()){
                int num1=num+1;
                while(s.find(num1)!=s.end()){
                    num1++;
                }
                ans=max(ans, num1-num);
            }
        }
        return ans;
    }
};