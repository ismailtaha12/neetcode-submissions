class Solution {
   public:
    vector<int> getConcatenation(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(2 * n);

        for (int i = 0; i < n; i++) {
            ans[i] = nums[i];
            ans[i + n] = nums[i];
        }
        return ans;
    }
};
// so nums length n 
// make ans of 2n
// ans[i] == nums[i] and ans[i+n] == nums[i]
// for 0 <= i < n
