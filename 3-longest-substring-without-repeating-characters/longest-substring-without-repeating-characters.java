class Solution {
    public int lengthOfLongestSubstring(String s) {
        int i = 0 , j = 0 , max = 0;
        HashSet<Character> hset = new HashSet();
        while(i<s.length()){
            if(!hset.contains(s.charAt(i))){
                hset.add(s.charAt(i));
                i++;
                max = Math.max(hset.size(),max);
            }else{
                hset.remove(s.charAt(j));
                j++;
            }
        }
        return max;
    }
}