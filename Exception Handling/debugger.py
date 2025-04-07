import pdb

def calculate_average(numbers):
    pdb.set_trace()  # <-- Start the debugger here
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return averag  # Typo!

def main():
    nums = [10, 20, 'thirty', 40]  # Error here!
    result = calculate_average(nums)
    print("The average is:", result)

main()
