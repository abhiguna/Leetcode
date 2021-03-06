class Solution {
    
    // Time = O(1)
    // Space = O(1)
    public int getSum(int a, int b) {
        while (b != 0) {
            int temp = a;
            a = a ^ b;
            b = temp & b;
            b <<= 1;
        }
        return a;
    }
}