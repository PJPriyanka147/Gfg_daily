#Problem Statement - Given an array arr[] of size N and an integer K. 
#Find the maximum for each and every contiguous subarray of size K.

#Brute Force --
def max_of_subarrays(arr, n, k):
    result = []
    for i in range(n - k + 1):
        max_value = arr[i]
        for j in range(1, k):
            if arr[i + j] > max_value:
                max_value = arr[i + j]

        result.append(max_value)
    
    return result


arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter K: "))
result = max_of_subarrays(arr, len(arr), k)
print(result)