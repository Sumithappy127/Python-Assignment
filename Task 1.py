def calculate_area(length, width):
    if length == width:
        return "This is a square!"
    else:
        return length * width

def main():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))

    result = calculate_area(length, width)

    if isinstance(result, str):
        print(result)
    else:
        print("The area of the rectangle is:", result)

main()
