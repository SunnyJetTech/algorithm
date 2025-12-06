def selection_sort(arr: list[int]) -> None:
    n = len(arr)
    
    if n <= 1: 
        return
    
    for idx in range(n - 1):
        min_idx = idx
        
        for idx2 in range(idx + 1, n):
            if arr[idx2] < arr[min_idx]:
                min_idx = idx2
                
        
        arr[idx], arr[min_idx] = arr[min_idx], arr[idx]
    
        
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    selection_sort(arr)
    print("Sorted array is:", arr)