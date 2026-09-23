class Solution {
public:
    bool isSubsequence(string s, string t) {
        int nt = t.size();
        int ns = s.size();
        int j = 0;
        for (int i = 0; i < nt; i++) {

            if(s[j] == t[i]){
                j++;
                if (j == ns) {
                    return true;
                }
            }
        }
        return false;
    }
};

// letters in relative order only
// check if s in t 
// while s in t -- until n of s ? 