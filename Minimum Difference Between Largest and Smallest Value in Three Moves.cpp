class Solution {
public:
    int minDifference(vector<int>& nums) {
        int n = nums.size();
        
        // cout << "n: " << n << endl;
        
        //after removing 3 elements, there will be at most one element
        if(n <= 4) return 0;
        
        /*
        looking at [nums.begin(), nums.end()),
        and make sure [nums.begin(), nums.begin()+4) is sorted
        */
        partial_sort(nums.begin(), nums.begin()+4, nums.end());
        /*
        looking at [nums.begin()+4, nums.end()),
        and make sure nth position has the right number,
        also elements before nth element are all <= nth element,
        and elements afater nth element are all >= nth element
        */
        nth_element(nums.begin()+4, nums.end()-4, nums.end());
        //now [nums.end()-4, nums.end()] are in right position
        
        //sort [nums.end()-4, nums.end()]
        sort(nums.end()-4, nums.end());
        
        int minDiff = INT_MAX;
        
        for(int i = 0; i <= 3; ++i){
            minDiff = min(minDiff, nums[n-1-i] - nums[3-i]);
        }
        
        return minDiff;
        
    }
};
