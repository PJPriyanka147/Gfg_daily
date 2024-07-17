#Problem Statement - Given two sorted arrays arr1 and arr2 of size N and M respectively and an element K. 
#The task is to find the element that would be at the kth position of the final sorted array.

#Brute Force --
def KthElement(arr1, arr2, n, m, k):
    merged = []
    i = j = 0

    while i < n and j < m:
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    while i < n:
        merged.append(arr1[i])
        i += 1
    
    while j < m:
        merged.append(arr2[j])
        j += 1

    return merged[k - 1]

arr1 = list(map(int, input("Enter elements of array 1: ").split()))
arr2 = list(map(int, input("Enter elements of array 2: ").split()))
kth_element = int(input("Enter K: "))
result = KthElement(arr1, arr2, len(arr1), len(arr2), kth_element)
print(result)
