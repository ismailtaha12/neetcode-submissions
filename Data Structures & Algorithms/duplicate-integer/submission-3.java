

class Solution {
    public boolean hasDuplicate(int[] nums) {
        
      
        HashSet<Integer> myNumber = new HashSet<Integer>();

        for(int num:nums){
            
if(myNumber.contains(num)) return true;

else myNumber.add(num);
        }
    return false;
    }
}