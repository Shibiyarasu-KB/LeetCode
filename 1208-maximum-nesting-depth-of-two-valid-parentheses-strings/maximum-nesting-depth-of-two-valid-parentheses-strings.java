class Solution {
    public int[] maxDepthAfterSplit(String seq) {
        int count=0;
        int[] arr=new int[seq.length()];
        for(int i=0;i<seq.length();i++){
        if(seq.charAt(i)=='('){
            arr[i]=count++ % 2;
        }else{
            arr[i]=--count %2;
        }
        }
        return arr;
    }
}