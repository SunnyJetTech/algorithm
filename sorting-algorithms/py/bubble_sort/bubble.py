def bubble_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    
    if n <= 1:
        return arr
    
    for idx in range(n):
        swapped = False
        
        for element in range(0, n - idx - 1):
             if arr[element] > arr[element + 1]:
                 arr[element], arr[element + 1] = arr[element + 1], arr[element]
                 swapped = True
                 
        if not swapped:
            break
        
    return arr
        
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90] 

    bubble_sort(arr)
    
    print(arr)
                 
                 
    