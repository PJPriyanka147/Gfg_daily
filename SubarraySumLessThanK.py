#Problem Statement - Given an array of positive numbers, the task is to find the number 
#of possible contiguous subarrays having product less than a given number k.

#Brute Force --
def sumLessThan_K(arr,n, k):
    count = 0
    for start in range(n):
        product = 1
        for end in range(start, n):
            product *= arr[end]

            if product < k:
               count += 1
            else:
                break

    return count 

arr = list(map(int, input("Enter elements of array:").split()))
k = int(input("Enter K:"))
result = sumLessThan_K(arr, len(arr), k)
print(result)