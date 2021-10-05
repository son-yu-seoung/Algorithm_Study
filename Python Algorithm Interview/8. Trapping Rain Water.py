# 42. Trapping Rain Water
# Q. Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example 1:
# Input : height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output : 6
# Explanation : The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Example 2 :
# Input : height = [4,2,0,3,2,5]
# Output : 9

# My solution O(n^2)
height = [0, 1, 0, 2, 1, 0, 1, 3]
m_height = max(height)
available_water = 0
        
while m_height > 0: # len(height)가 아니라 m_height는 10000 일수도 있다. 즉, 여기서도 많은 시간을 소요한다.
    length = [idx for idx, value in enumerate(height) if value >= m_height]

            
    if len(length) < 2:
        m_height -= 1 # -1로 하면 너무큰 시간 낭비가 있을 수 있다. 
        continue
            
    available_water += - length[0] + length[-1] - (len(length)-1) # calculation result 
    m_height -= 1
        
print(available_water)
 
# 왼쪽과 오른쪽이 나의 idx의 value보다 1크면 water + 1, 많이 크다면 쌍이 있는지 확인
avaliable_water = 0
queue = [] # FIFO
for i in range(1, len(height)-1):
    v = height[i] # middle
    left, right = height[i-1], height[i+1]

    if left > v and right > v:
        l_v, r_v = left - v, right - v

        if r_v > l_v:
            avaliable_water += 1 * l_v
        elif r_v == l_v:
            avaliable_water += 1 * r_v # or l_v
        elif r_v < l_v:
            avaliable_water += 1 * r_v

print(avaliable_water)


    


        