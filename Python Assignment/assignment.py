import math
class Solution:
    def sumPrimeNumbers(self,a:int,b:int):
        if(b<a):
            return 0
            
        def prime(n:int):
            if(n<2):
                return False
            for i in range(2,int(math.sqrt(n)+1)): 
                if(n%i==0):
                    return False       
            return True
        
        totalSum=0
        for num in range(a,b+1):
            if prime(num):
                totalSum+=num
        return totalSum
    
    def smallestSum(self,nums:list[int]):
        #Assuming the size of subarray 3
        totalSum = 0
        window = 3
        for i in range(0,window):
            totalSum += nums[i]
        
        maximum = totalSum
        for i in range(1,len(nums)-window+1):
            totalSum = totalSum - nums[i-1] + nums[i+window-1]
            if totalSum < maximum:
                maximum = totalSum
        return maximum
            
    
    def thirdSmallestNumber(self,nums:list[int]):
        # If sorting was allowed we could sort the elements and return nums[2]
        
        if len(nums)<3:
            return None
        
        smallest = float('inf')
        s_small=float('inf')
        t_small=float('inf')

        for num in nums:
            if num<smallest:
                t_small = s_small
                s_small = smallest
                smallest = num
            elif smallest<num<s_small:
                t_small=s_small
                s_small=num
            elif s_small<num<t_small:
                t_small =num
        return t_small if t_small!=float('inf') else None 

solution = Solution()
nums=[50,42,15,3,1,25,78,91]
a=10
b=20
print(f"Sum of prime numbers between {a} and {b}: ",solution.sumPrimeNumbers(a,b))
print("Minimum sum of all integers in the subarray is :",solution.smallestSum(nums))
print("Third smallest number in the given array is: ", solution.thirdSmallestNumber(nums))
