class Solution {
    
    public int num_ones(int num) {
        int count = 0;
        
        // Set rightmost bit to 0 until num becomes 0
        while (num != 0) {
            count++;
            num = (num & (num - 1));
        }
        
        return count;
    }
    
    // Time = O(N)
    // Space = O(1)
    public int[] countBits(int n) {
        int[] res = new int[n+1];
        
        for (int i = 0; i < n + 1; i++) {
            res[i] = num_ones(i);
        }
        
        return res;
    }
}