class Solution {
 public:
  bool isAnagram(string s, string t) {
    if (s.size() != t.size()) {
      return false;
    }
    int n = s.size();
    vector<int> count(26, 0);

    for (int i = 0; i < n; i++) {
      count[s[i] - 'a']++;
      count[t[i] - 'a']--;
    }

    for (auto& val : count) {
      if (val != 0) {
        return false;
      }
    }
    return true;
  }
};
