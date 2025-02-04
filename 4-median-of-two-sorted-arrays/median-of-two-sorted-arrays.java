class Solution {
    public double findMedianSortedArrays(int[] a, int[] b) {
        int[] c=new int[a.length+b.length];// array creation in by 2 array length
        System.arraycopy(a,0,c,0,a.length);// copy array to another array
        System.arraycopy(b,0,c,a.length,b.length);
        Arrays.sort(c);//inbuilt method to sort array
        if(c.length%2==0){
            return (c[c.length / 2] + c[c.length / 2 - 1]) / 2.0;
        }else{
            return c[c.length/2];
        }
    }
}