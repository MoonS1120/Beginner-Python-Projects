from random import randint

values = [randint(1,10) for _ in range(10)]
target_value = int(input("Target value: "))
sorted_values = sorted(list(set(values)))

def binary_search(values, target):
    low = 0
    high = len(values) - 1

    while low <= high:
        midpoint = (low + high) // 2
        if values[midpoint] == target:
            return midpoint
        elif values[midpoint] > target:
            high = midpoint - 1
        else:
            low = midpoint + 1
    return False

if __name__ == "__main__":
    print(sorted_values)
    result = binary_search(sorted_values, target_value)
    if result is False:
        print("Target value not found.")
    else:
        print("Target value found at index:", result)
