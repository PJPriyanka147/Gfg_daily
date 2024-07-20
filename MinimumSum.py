#Problem Statement - Given an array Arr of size N such that each element is from the range 0 to 9.
#Find the minimum possible sum of two numbers formed using the elements of the array. All digits in
#the given array must be used to form the two numbers.

def minimum_sum(arr, n):
    arr.sort()
        
    num1 = []
    num2 = []
        
    for i in range(n):
        if i % 2 == 0:
            num1.append(arr[i])
        else:
            num2.append(arr[i])
        
    number1 = int(''.join(map(str, num1)))
    number2 = int(''.join(map(str, num2)))
        
    min_sum = str(number1 + number2)
        
    return min_sum

arr = list(map(int, input("Enter elements of array: ").split()))
result = minimum_sum(arr, len(arr))
print(result)
