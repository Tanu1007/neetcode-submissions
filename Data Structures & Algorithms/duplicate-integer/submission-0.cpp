class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> newset(nums.begin(), nums.end());
        return newset.size()<nums.size();
    }
};