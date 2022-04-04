class Solution {
    
    // Time = O(N)
    // Space = O(1)
    public int[] countBits(int n) {
        int[] res = new int[n+1];
        
        for (int i = 1; i < n + 1; i++) {
            res[i] = res[i & (i-1)] + 1;
        }
        
        return res;
    }
}