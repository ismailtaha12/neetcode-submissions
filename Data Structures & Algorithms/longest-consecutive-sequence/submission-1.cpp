class Solution {
 public:
  int longestConsecutive(vector<int>& nums) {
    unordered_set<int> numSet(nums.begin(), nums.end());
    int longest = 0;

    for (int n : numSet) {
      // Only begin counting at the start of a sequence
      if (numSet.find(n - 1) == numSet.end()) {
        int length = 1;

        while (numSet.find(n + length) != numSet.end()) {
          length++;
        }

        longest = max(longest, length);
      }
    }

    return longest;
  }
};

// longest sequence of nums[n] and nums[n+1]
// sort then count
//  two loops one for longest seq and one for the seq

// to start a new seq check that no other n-1
// while search for n+1 ==true increment length