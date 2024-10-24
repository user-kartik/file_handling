def insert_into_sorted_list(arr, element):
    
    i = 0
    while i < len(arr) and arr[i] < element:
        i += 1

    arr.insert(i, element)
    return arr

# Example usage:
arr = [1, 3, 5, 7, 9]
element = int(input("Enter the element to insert: "))

result = insert_into_sorted_list(arr, element)
print("List after insertion:", result)
