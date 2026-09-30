class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        priority_queue<pair<int, int>> maxHeap; //frequency
        //map<number, frequency>;
        unordered_map<int, int> map;
        for(int i=0;i<nums.size();i++){
            map[nums[i]]++;
        }
        for(auto& pair: map){
            maxHeap.push({pair.second, pair.first});
        }
        vector<int> ans;
    
        for(int i=0;i<k;i++){
            ans.push_back(maxHeap.top().second);
            maxHeap.pop();
        }
        return ans;
    }
};
