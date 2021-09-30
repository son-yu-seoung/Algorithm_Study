# 42. Trapping Rain Water
# Q. Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example 1:
# Input : height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output : 6
# Explanation : The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Example 2 :
# Input : height = [4,2,0,3,2,5]
# Output : 9

# My solution 
Input = [0, 1, 0, 2, 1, 0, 1, 3]
m_val = max(Input)
available_water = 0

while m_val > 0:
    width = [idx for idx, value in enumerate(Input) if value >= m_val] # Important!!! 
    
    if len(width) < 2:
        m_val -= 1
        continue 
    
    for i in range(len(width)-1):
        avaliab_water += width[i+1] - width[i] - 1
    
    m_val -= 1 

print(avaliab_water)
        
        