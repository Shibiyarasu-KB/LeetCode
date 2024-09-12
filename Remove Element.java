import java.util.*;

class Solution {
    public int removeElement(int[] nums, int val) {
        int index = 0; // Pointer for the new position
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[index++] = nums[i]; // Place element at new index
            }
        }
        return index; // Return the length of the new array
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> arrayList = new ArrayList<>();
        
        System.out.println("Enter the elements of the array (type a non-integer to stop):");
        while (sc.hasNextInt()) {
            int num = sc.nextInt();
            arrayList.add(num);
        }
        sc.nextLine();

        System.out.print("Enter the element to remove: ");
        int val = sc.nextInt();

        // Convert ArrayList to an array
        int[] arr = arrayList.stream().mapToInt(i -> i).toArray();

        Solution solution = new Solution();

        int newLength = solution.removeElement(arr, val); // Correctly handle the return type

        // Print the array up to the new length
        System.out.println(newLength + Arrays.toString(Arrays.copyOf(arr, newLength)));
    }
}
