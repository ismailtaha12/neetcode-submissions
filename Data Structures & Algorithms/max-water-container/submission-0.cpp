class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0;
        int r = heights.size() - 1;
        int maxarea = -1;
        while (l < r) {

            int  w = r - l;
            int h = min (heights[l] , heights[r]);
            int area = w * h;
            maxarea = max(area,maxarea);
            if (heights[l] < heights[r]) {
                l++;
            }else{
                r--;
            }
            
        }
        return maxarea;
    }
};

// heights each hegihts[i] is height of ith break
// select two ith  bars to form greatest area 

// two pointer while bigger move smaller
// w = d2 - d1
// h = min (height[l] , height[r])
// area = w * h 
// maxarea = max(area,maxarea)
// return maxarea


