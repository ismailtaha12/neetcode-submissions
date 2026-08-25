class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        
        HashMap<String, List<String>> table = new HashMap<String, List<String>>();



            for(String str : strs){
            int[] count = new int[26];


            for(char ch : str.toCharArray()){

                count[ch -'a']++;
            }
            String key = Arrays.toString(count);
            table.putIfAbsent(key, new ArrayList<>());
            table.get(key).add(str);
            }
            return new ArrayList<>(table.values());

    }
}
