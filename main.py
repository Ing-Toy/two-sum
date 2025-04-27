from typing import List

def twoSum(nums:List[int], target:int)-> List[int]:
    suma = 0
    for i in nums:
        suma = i
        temp = nums.copy()
        temp.remove(i)
        for b in temp:
            suma+=b
            if (suma == target):
                return [nums.index(i),nums.index(b)]
            suma-=b
        temp.clear()
        suma=0
    return 
