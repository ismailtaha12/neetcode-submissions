

class Solution {
    public boolean hasDuplicate(int[] nums) {
        
        int x = nums.length;
        HashSet<Integer> myNumber = new HashSet<Integer>();

        for(int num:nums){
            myNumber.add(num);

        }

        if(x!=myNumber.size()){
            return true;
        }
        return false;

    }
}