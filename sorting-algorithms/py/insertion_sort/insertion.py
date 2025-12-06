def insertion_sort(arr: list[int]) -> None:
    if len(arr) <= 1: 
        return
    
    for index in range(1, len(arr)):
        key = arr[index]
        prev_index = index - 1
        
        while prev_index >= 0 and key < arr[prev_index]:
            arr[prev_index + 1] = arr[prev_index]
            prev_index -= 1
            
        arr[prev_index + 1] = key
        
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    insertion_sort(arr)
    print(arr)
        
        
        
    
    