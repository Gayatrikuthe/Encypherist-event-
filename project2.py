def three_sum(nums):
    # Sort the array to facilitate the two-pointer approach
    nums.sort()
    result = []
    
    # Traverse the array
    for i in range(len(nums) - 2):
        # Skip duplicate values to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Set two pointers
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for the left pointer
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicates for the right pointer
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                # Move the pointers
                left += 1
                right -= 1
                
            elif total < 0:
                # If the sum is less than zero, move the left pointer to the right
                left += 1
            else:
                # If the sum is greater than zero, move the right pointer to the left
                right -= 1
    
    return result


nums = [-1, 0, 1, 2, -1, -4]
triplets = three_sum(nums)
print(triplets)
