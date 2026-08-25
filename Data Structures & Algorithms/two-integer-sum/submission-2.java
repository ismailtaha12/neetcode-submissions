class Solution {
    public int[] twoSum(int[] nums, int target) {
        

        HashMap<Integer,Integer> table = new HashMap<Integer,Integer>();
        
        for(int i =0;i < nums.length;i++){

                int diff = target - nums[i];
                if(table.containsKey(diff)){

                return new int[] { table.get(diff), i }; 
                // return indices
                }           
                
                table.put(nums[i] , i);
        }
        return new int[] {}; // or throw exception if no solution
    }
}
