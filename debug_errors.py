def calculate_average(numbers):
    try:
        total = 0
        for i in range(len(numbers)):
            total += numbers[i]
        return total / len(numbers)

    except ZeroDivisionError:
        print("Warning: Cannot have average of an empty list. Returning 0.")
        return 0
    
def get_list_element(my_list, index):
    try:
        return my_list[index]

    except IndexError:
        print(f"Error: Index {index} is out of bounds.")
        return None

    except TypeError:
        print("Error: The first argument must be a list.")
        return None

data1 = [10, 20, 30, 40, 50]
data2 = [5, 15]
data3 = [] 
print(f"Average of data1: {calculate_average(data1)}")
print(f"Average of data2: {calculate_average(data2)}")
print(f"Average of data3: {calculate_average(data3)}")

print("\nValid index inputs:", get_list_element([60, 70, 80], 1))
print("Out-of-bounds inputs:", get_list_element([1, 10, 20], 2))
print("Incorrect type inputs:", get_list_element(12345, 10))