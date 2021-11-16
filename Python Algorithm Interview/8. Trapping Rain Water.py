# 42. Trapping Rain Water
# Q. Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example 1:
# Input : height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output : 6
# Explanation : The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Example 2 :
# Input : height = [4,2,0,3,2,5]
# Output : 9

# My solution O(n^2) <- Time Limit Exceeded !!!
class Solution:
    def trap(self, height: List[int]) -> int:
        m_height = max(height)
        available_water = 0

        while m_height > 0: # len(height)가 아니라 m_height는 10000 일수도 있다. 즉, 여기서도 많은 시간을 소요한다.
            length = [idx for idx, value in enumerate(height) if value >= m_height]


            if len(length) < 2:
                m_height -= 1 # -1로 하면 너무큰 시간 낭비가 있을 수 있다. 이 방법만 바꿔도 해결 될 듯?
                continue

            available_water += - length[0] + length[-1] - (len(length)-1) # calculation result 
            m_height -= 1
            
        return available_water

# Other solution - Two Pointer O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)

            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1

            else:
                volume += right_max - height[right]
                right -= 1
        
        return volume

# Other solution - Stack
class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            # 변곡점을 만나는 경우
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()

                if not len(stack):
                    break

                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters

            stack.append(i)
        
        return volume

 


    


        