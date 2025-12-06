def insert(arr: list[int]):
    if len(arr) <= 1: return arr
    
    for element in range(1, len(arr)):
        key = arr[element]
        Prev_element = element - 1
        
        while Prev_element >= 0 and key < arr[Prev_element]:
            arr[Prev_element + 1] = arr[Prev_element]
            Prev_element -= 1
        arr[Prev_element + 1] = key

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    insert(arr)
    print(arr)