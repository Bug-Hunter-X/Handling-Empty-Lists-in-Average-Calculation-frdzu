def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

my_list = [10, 20, 30, 40, 50]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

#Additional test cases for robustness
my_list2 = [1,2,3,4,5,6,7,8,9,10]
average2 = calculate_average(my_list2)
print(f"The average of my_list2 is: {average2}")

my_list3 = []
average3 = calculate_average(my_list3)
print(f"The average of my_list3 is: {average3}")

my_list4 = [100]
average4 = calculate_average(my_list4)
print(f"The average of my_list4 is: {average4}") 