public class Solution {
    // you need to treat n as an unsigned value
    
    // Time = O(1)
    // Space = O(1)
    public int hammingWeight(int n) {
        int num_ones = 0;
        int mask = 1;
            
        for (int i = 0; i < 32; i++) {
            if ((n & mask) != 0) {
                num_ones++;
            }
            mask = mask << 1;
        }
        
        return num_ones;
    }
}