def check_number(num):
    if num > 7:
        print("Hello")
    else:
        print("The number is not greater than 7")

def check_name(name):
    if name == "John":
        print("Hello, John")
    else:
        print("There is no such name")

def process_array(array):
    multiples_of_three = [x for x in array if x % 3 == 0]
    print("Elements that are multiples of 3:", multiples_of_three)

# Main Program with Interactive Input
if __name__ == "__main__":
    # Input number and process
    try:
        number = int(input("Enter a number: "))
        check_number(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

    # Input name and process
    name = input("Enter a name: ")
    check_name(name)

    # Input array and process
    try:
        array = list(map(int, input("Enter a numeric array (space-separated): ").split()))
        process_array(array)
    except ValueError:
        print("Invalid input. Please enter numbers only.")
