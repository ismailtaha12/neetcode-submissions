class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        already_satisfied = 0

        for i in range(len(customers)):
            if grumpy[i] == 0:
                already_satisfied += customers[i]
        

        extra = 0
        maxExtra = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                already_satisfied += customers[i]
        
        left = 0
        right = minutes

        while right < len(customers):
            if grumpy[right] == 1:
                extra += customers[right]

            if grumpy[left] == 1:
                extra -= customers[left]

            maxExtra = max(extra, maxExtra)
            left +=1
            right +=1
        
        return already_satisfied + maxExtra
        






        


        
        