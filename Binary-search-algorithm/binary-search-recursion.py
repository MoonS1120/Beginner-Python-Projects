from random import randint

values = [randint(1,10) for _ in range(10)]
target_value = int(input("Target value: "))
sorted_values = sorted(list(set(values)))

def binary_search(values, target, start_index=0):
    midpoint = len(values) // 2

    if len(values) == 0:
        return False

    if values[midpoint] == target:
        return midpoint + start_index
    elif values[midpoint] > target:
        return binary_search(values[:midpoint], target, start_index)
    else:
        return binary_search(values[midpoint+1:], target, start_index + midpoint + 1)
    

if __name__ == "__main__":
    print(sorted_values)
    result = binary_search(sorted_values, target_value)
    if result is False:
        print("Target value not found.")
    else:
        print("Target value found at index:", result)
