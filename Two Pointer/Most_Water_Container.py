class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = len(height)
        left = 0
        right = l - 1
        maxi = 0

        while(left<right):
            capacity = min(height[left],height[right])*(right-left)
            maxi = max(capacity,maxi)

            if(height[left]>height[right]):
                right-=1
            else:
                left+=1

        return maxi
