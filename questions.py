from typing import List

# Find the maximum sum of a subarray (Kadane's Algorithm).

def max_sum(nums: list):
    i:int = 0 
    j : int = 0 
    longest:int = 0
    sum_:int = 0
    while j < len(nums):    
        sum_+=nums[j]
        if sum_ > longest : 
            longest = sum_
        if sum_ < longest :
            sum_-=nums[i]
            i+=1
        j+=1
    return longest

# Rotate an array by k steps.

def roatate_byk(nums:list[int] , k :int):
    nums.reverse()

    s = 0 
    e = k-1
    while s < e :
        nums[s],nums[e] = nums[e],nums[s]
        s+=1
        e-=1

    end = len(nums)-1
    while k < end :
        nums[k],nums[end] = nums[end],nums[k]
        k+=1
        end-=1
    return nums

print(roatate_byk([1,2,3,4],2))



# Find the longest substring without repeating characters.


def longest_sub(s: str) -> int:
    window = [] 
    i = 0 
    longest = 0  

    for e in range(len(s)):  
        while s[e] in window:
            window.remove(s[i]) 
            i += 1  

        window.append(s[e])

        longest = max(longest, e - i + 1)

    return longest

print(longest_sub("hello"))


# Search for a target in a sorted and rotated array.


# Merge two sorted arrays.

def findindex(n: list , num):
    for i in range(1,len(n)-1):
        if n[i-1] < num and n[i+1] > num:
            return i

def merge(n1: list, n2: list):
    for i in n2:
        idx = findindex(n1, i)
        if idx is not None:  # Check if an index was found
            n1.insert(idx, i)  # Insert element at the found index
    return n1
    

print((merge([1,3,5],[2,4])))

