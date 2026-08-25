class Solution {
    public boolean hasDuplicate(int[] nums) {
        
        Set<Integer> uniqueElements = new HashSet<>();

        for (int num : nums) {
            uniqueElements.add(num);
        }
        
        return uniqueElements.size() != nums.length;

    }
}